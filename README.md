# Ultimate-Python-Fitness-Tracker
# 🔥 Personal Fitness Tracker  

A **machine learning-powered fitness tracking application** built using **Streamlit** that helps users predict the **calories burned** based on input parameters like age, BMI, heart rate, and workout duration.  

---

## 🚀 Problem Statement  

In today's fast-paced world, tracking fitness progress and estimating **calories burned** is essential for maintaining a healthy lifestyle. However, most people lack access to accurate, **data-driven** calorie estimation models.  
**This project aims to solve this problem** by leveraging **Machine Learning** to predict calorie expenditure based on user inputs like age, BMI, heart rate, and exercise duration.  
---
## ✅ Best Used Approach  

To achieve **highly accurate calorie predictions**, this project follows a **data-driven approach** utilizing:  
✔ **Random Forest Regressor** - Chosen for its **high accuracy** and ability to handle **non-linear relationships** in fitness data.  
✔ **Feature Engineering** - Created a **BMI feature** (Weight/Height²) to improve model performance.  
✔ **One-Hot Encoding for Gender** - Converted categorical data into numerical format for better predictions.  
✔ **Data Normalization** - Ensured all numerical inputs were properly scaled.  
---

## 🧑‍🔬 Methodology Used  

This project follows the **end-to-end machine learning workflow**, including:  
### 🔹 **1. Data Collection & Cleaning**  
- Used **calories.csv** and **exercise.csv** datasets  
- Merged datasets based on **User_ID**  
- Removed unnecessary columns for optimal processing  

### 🔹 **2. Feature Engineering**  
- Created **BMI** column for better fitness analysis  
- One-Hot Encoding for categorical **gender** column  

### 🔹 **3. Model Selection & Training**  
- **Train-Test Split** (80%-20%)  
- Chose **Random Forest Regressor** due to its ability to handle non-linearity  
- **Hyperparameter tuning** for best accuracy  

### 🔹 **4. Deployment with Streamlit**  
- Created an interactive UI using **Streamlit**  
- Used **Streamlit Forms** for better input handling  
- Added **Balloon animations** for a fun user experience  

---

## 💻 How to Run the Application  

### **🔹 Step 1: Clone the Repository**
```bash
git clone https://github.com/Harikrishna772003/Ultimate-Python-Fitness-Tracker.git
cd Ultimate-Python-Fitness-Tracker
           OR
use the below link to view my project application
copy&paste url to view
https://ultimate-python-fitness-tracker-43hphml9hw6heisghhvmsn.streamlit.app/
