<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=800&size=32&duration=3500&pause=1500&color=FC466B&center=true&vCenter=true&width=900&height=70&lines=%F0%9F%92%AA%20Smart%20Fitness%20Tracker" alt="Smart Fitness Tracker"/>

<b><i>ML-powered personalised fitness & diet recommendations</i></b>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=36BCF7&center=true&vCenter=true&width=700&lines=%F0%9F%92%AA%20Personalised%20workout%20plans;%F0%9F%A5%97%20Diet%20recommendations;%F0%9F%A4%96%20A%20systematic%20ML%20approach" alt="Typing SVG" />

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn"/> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/> <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>

<img src="https://img.shields.io/github/stars/PreciousBharath/FITNESS-TRACKER?style=social" alt="stars"/> <img src="https://img.shields.io/github/forks/PreciousBharath/FITNESS-TRACKER?style=social" alt="forks"/> <img src="https://img.shields.io/github/last-commit/PreciousBharath/FITNESS-TRACKER?style=flat-square&color=blueviolet" alt="last commit"/> <img src="https://img.shields.io/github/repo-size/PreciousBharath/FITNESS-TRACKER?style=flat-square&color=success" alt="repo size"/>
</div>

---

## 💪 About the Project

Inspired by *“A Systematic Machine Learning Approach in Fitness Platforms”*, this app analyses a user's profile — sex, age, height, weight, BMI, hypertension, diabetes, level and fitness goal — and recommends **exercises, equipment, diet and fitness type** using a trained ML model.

## ✨ Key Features

- 🔐 Login and personal **dashboard**
- 🏋️ Recommends **exercises, equipment & fitness type**
- 🥗 Suggests a matching **diet plan**
- 🗄️ Saves prediction history in **SQLite** (`predictions.db`)
- 📓 Full training notebook `Fitness Tracker.ipynb`

## 🧠 How It Works

```mermaid
flowchart LR
U["🧍 Body Profile + Goal"] --> E["🔤 Label Encoders"] --> M["🤖 ML Model"] --> R["🏋️ Workout + 🥗 Diet Plan"]
```

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Data & ML | Pandas · NumPy · scikit-learn |
| Notebook | Jupyter |
| Web App | Flask + Jinja2 templates |
| Frontend | HTML5 · CSS3 |
| Database | SQLite |

## 📂 Project Structure

```text
├── abstract/ · basepaper/
└── code/Fitness Tracker/
    ├── app.py
    ├── Fitness Tracker.ipynb
    ├── fitness-recommendation-dataset.xlsx
    ├── model.pkl + le_*.pkl encoders
    ├── predictions.db
    └── templates/ (home, login, dashboard, prediction, ...)
```

## 🚀 Getting Started

```bash
git clone https://github.com/PreciousBharath/FITNESS-TRACKER.git
cd "FITNESS-TRACKER/code/Fitness Tracker"
pip install flask pandas numpy scikit-learn openpyxl
python app.py
```

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Feel free to ⭐ star the repo and open a pull request.

## 👨‍💻 Author

<div align="center">

**Bharath** — Software Developer · Project Engineer · Technical Trainer

<a href="https://github.com/PreciousBharath"><img src="https://img.shields.io/badge/GitHub-PreciousBharath-181717?style=for-the-badge&logo=github"/></a>
<a href="https://linkedin.com/in/connectbharath"><img src="https://img.shields.io/badge/LinkedIn-connectbharath-0A66C2?style=for-the-badge&logo=linkedin"/></a>

### 🍔 EAT · 💻 CODE · 😴 SLEEP · 🔁 REPEAT

⭐ **If you found this project useful, give it a star!** ⭐

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

</div>
