from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
import sqlite3
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = "your_secret_key"

# ===================== LOAD MODELS AND ENCODERS =====================
model = joblib.load("model.pkl")
le_sex = joblib.load("le_sex.pkl")
le_hypertension = joblib.load("le_hypertension.pkl")
le_diabetes = joblib.load("le_diabetes.pkl")
le_level = joblib.load("le_level.pkl")
le_fitness_goal = joblib.load("le_fitness_goal.pkl")
le_fitness_type = joblib.load("le_fitness_type.pkl")
le_exercises = joblib.load("le_exercises.pkl")
le_equipment = joblib.load("le_equipment.pkl")
le_diet = joblib.load("le_diet.pkl")
le_recommendation = joblib.load("le_recommendation.pkl")

# ===================== INITIALIZE DATABASE =====================
conn = sqlite3.connect('predictions.db', check_same_thread=False)
c = conn.cursor()

# Create users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')

# Create predictions table
c.execute('''
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    date TEXT,
    sex TEXT,
    age INTEGER,
    height REAL,
    weight REAL,
    bmi REAL,
    level TEXT,
    fitness_goal TEXT,
    fitness_type TEXT,
    exercises TEXT,
    equipment TEXT,
    diet TEXT,
    recommendation TEXT
)
''')
conn.commit()

# ===================== ROUTES =====================

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('prediction'))
    return render_template('home.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        c.execute('SELECT * FROM users WHERE username=?', (username,))
        user = c.fetchone()

        if user and user[2] == password:
            session['username'] = username
            flash("Logged in successfully!", "success")
            return redirect(url_for('prediction'))
        else:
            flash("Invalid credentials", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash("Enter both username and password", "warning")
            return redirect(url_for('register'))

        c.execute('SELECT * FROM users WHERE username=?', (username,))
        existing_user = c.fetchone()
        if existing_user:
            flash("Username already exists", "danger")
            return redirect(url_for('register'))

        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        flash("Registration successful! Please login.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("Logged out successfully!", "success")
    return redirect(url_for('home'))


@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if 'username' not in session:
        flash("Please login first", "warning")
        return redirect(url_for('login'))

    recommendation = None
    current_date = None

    # Get original classes for dropdowns
    sex_classes = le_sex.classes_
    hypertension_classes = le_hypertension.classes_
    diabetes_classes = le_diabetes.classes_
    level_classes = le_level.classes_
    goal_classes = le_fitness_goal.classes_
    type_classes = le_fitness_type.classes_
    exercises_classes = le_exercises.classes_
    equipment_classes = le_equipment.classes_
    diet_classes = le_diet.classes_

    if request.method == 'POST':
        # ===== Read form inputs =====
        sex = request.form['sex']
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        hypertension = request.form['hypertension']
        diabetes = request.form['diabetes']
        level = request.form['level']
        fitness_goal = request.form['fitness_goal']
        fitness_type = request.form['fitness_type']
        exercises = request.form['exercises']
        equipment = request.form['equipment']
        diet = request.form['diet']

        # ===== Calculate BMI =====
        bmi = weight / (height ** 2)

        # ===== Encode inputs including BMI =====
        X = np.array([
            le_sex.transform([sex])[0],
            age,
            height,
            weight,
            bmi,
            le_hypertension.transform([hypertension])[0],
            le_diabetes.transform([diabetes])[0],
            le_level.transform([level])[0],
            le_fitness_goal.transform([fitness_goal])[0],
            le_fitness_type.transform([fitness_type])[0],
            le_exercises.transform([exercises])[0],
            le_equipment.transform([equipment])[0],
            le_diet.transform([diet])[0]
        ]).reshape(1, -1)

        # ===== Predict recommendation =====
        pred_encoded = model.predict(X)[0]
        recommendation = le_recommendation.inverse_transform([pred_encoded])[0]

        # ===== Save prediction to DB =====
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute('''INSERT INTO predictions
                     (username, date, sex, age, height, weight, bmi, level, fitness_goal,
                      fitness_type, exercises, equipment, diet, recommendation)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                  (session['username'], current_date, sex, age, height, weight, bmi, level,
                   fitness_goal, fitness_type, exercises, equipment, diet, recommendation))
        conn.commit()

    return render_template('prediction.html',
                           recommendation=recommendation,
                           current_date=current_date,
                           sex_classes=sex_classes,
                           hypertension_classes=hypertension_classes,
                           diabetes_classes=diabetes_classes,
                           level_classes=level_classes,
                           goal_classes=goal_classes,
                           type_classes=type_classes,
                           exercises_classes=exercises_classes,
                           equipment_classes=equipment_classes,
                           diet_classes=diet_classes)


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash("Please login first", "warning")
        return redirect(url_for('login'))

    # Fetch user's predictions
    c.execute('SELECT date, bmi, level, fitness_goal, recommendation FROM predictions WHERE username=? ORDER BY date ASC', 
              (session['username'],))
    data = c.fetchall()

    bmi_values = []
    bmi_labels = []
    level_counts = {}
    goal_counts = {}
    rec_counts = {}

    for row in data:
        date, bmi, level, goal, rec = row
        bmi_values.append(round(bmi, 2))
        bmi_labels.append(date)

        level_counts[level] = level_counts.get(level, 0) + 1
        goal_counts[goal] = goal_counts.get(goal, 0) + 1
        rec_counts[rec] = rec_counts.get(rec, 0) + 1

    # Prepare chart data
    return render_template('dashboard.html',
                           bmi_values=bmi_values,
                           bmi_labels=bmi_labels,
                           level_labels=list(level_counts.keys()),
                           level_counts=list(level_counts.values()),
                           goal_labels=list(goal_counts.keys()),
                           goal_counts=list(goal_counts.values()),
                           rec_labels=list(rec_counts.keys()),
                           rec_counts=list(rec_counts.values()))



if __name__ == '__main__':
    app.run(debug=True)
