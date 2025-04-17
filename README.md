# 🐱 Cat Facts App

A fun web application that serves random cat facts via a Flask API and presents them with a cute cat image on the frontend. It also includes an automation script using Selenium to fetch the fact from the UI.

---

## 📁 Project Structure

Cat-Fact/ │ 
├── api/ # Flask backend API │ 
    ├── app.py │ 
    ├── cat_facts.py │ 
└── templates/ │ 
    └── home.html │ 
├── automation/ # Selenium automation script │ 
    ├── get_cat_fact.py │ 
    └── chromedriver # Chrome WebDriver (Linux) │ 
├── static/ # Static assets │   
    ├── css/ │ │ 
        └── home.css │ 
    └── images/ │ 
        └── cat.jpg │ 
├── venv/ # Python virtual environment 
└── README.md 



## 🚀 Features

- **Flask API**: Serves random cat facts via JSON.
- **Web UI**: Renders cat facts with an adorable cat image.
- **Selenium Automation**: Fetches and prints cat facts from the frontend using Chrome WebDriver.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MaiZakaria18/cat-facts.git
cd cat-facts
2. Create and Activate Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install flask selenium

cd api
python app.py

Visit: http://localhost:5000/home

🔌 API Endpoints

Route	Description
/home	Returns a webpage with a cat fact
/facts	Returns a random cat fact as JSON

🤖 Running the Selenium Script
Make sure Flask is running, then in a separate terminal:


cd automation
python get_cat_fact.py
The script will open Chrome, visit the webpage, wait for the fact to load, and print it in the terminal.

🧠 Notes
Ensure your chromedriver matches your local Chrome version.

