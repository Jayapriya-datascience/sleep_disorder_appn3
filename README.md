https://sleepdisorderappn3-bayekn33udywanltmka3xnfinally.streamlit.app/
finallyy
# sleep_disorder_appn3
# Project Overview
Smart Detection of Sleep Disorders Using Machine Learning is a web-based application designed to predict common sleep disorders such as Insomnia, Sleep Apnea, and Anxiety based on health and lifestyle-related inputs.

The system uses the XGBoost Classifier algorithm, which is known for its high performance and accuracy. To handle class imbalance in the dataset, it applies SMOTE (Synthetic Minority Over-sampling Technique) during training. The frontend is built using Streamlit, providing a clean and interactive user interface.

Users can:
-Enter personal and health data
-Instantly view the predicted sleep disorder
-Receive health tips
-Download a customized report in PDF format

This project aims to spread awareness about sleep disorders and provide a smart, accessible tool for early detection and prevention.

# Project Objectives
✅ Early Detection: Predict sleep disorders like Insomnia, Sleep Apnea, and Anxiety using machine learning techniques.

✅ User-Friendly Interface: Provide a simple and interactive Streamlit-based web app for easy access and usability.

✅ Health Awareness: Offer personalized health tips based on user input to promote better sleep habits.

✅ Report Generation: Allow users to download a summary of their inputs, prediction, and suggestions in PDF format.

✅ Data-Driven Solution: Use real-world health and lifestyle data to build a reliable and accurate predictive model.

✅ Address Class Imbalance: Apply SMOTE to improve model performance on under-represented sleep disorder cases.

 # ❗ Problem Statement
Sleep disorders like Insomnia, Sleep Apnea, and Anxiety are increasingly common due to modern lifestyle factors such as stress, poor sleep habits, and lack of physical activity. Many individuals remain undiagnosed because early symptoms are often ignored or go unnoticed.
Traditional detection methods are time-consuming, expensive, and not easily accessible to everyone.

# 💡 Proposed Solution
This project offers a smart, AI-powered web application that helps users identify the risk of sleep disorders by simply entering a few health and lifestyle-related details.
The solution includes:

-**A machine learning model (XGBoost Classifier)** for accurate predictions.
-**SMOTE** to handle class imbalance and improve detection of minority cases.
-A clean and simple **Streamlit interface** for easy use.
-**Health tips** based on prediction results.
-Option to **download a PDF report** for personal reference or to share with a doctor.

This system provides a quick, accessible, and user-friendly way to raise awareness and encourage early treatment of sleep-related issues.

# 🔄 Workflow of the Project
Below is the step-by-step workflow followed in the project:

# 1.📥 Data Collection

Loaded the sleep disorder dataset (CSV format) containing health and lifestyle features.

# 2.🧹 Data Preprocessing

-Handled missing values and removed duplicates.
-Applied Label Encoding for categorical columns.
-Normalized data using MinMaxScaler.

# 3.⚖️ Handling Class Imbalance

Applied SMOTE (Synthetic Minority Over-sampling Technique) to balance the dataset.

# 4.🤖 Model Training

-Used the XGBoost Classifier algorithm to train the model.
-Performed train-test split to evaluate performance.

# 5.✅ Model Evaluation

-Evaluated accuracy, precision, recall, and F1-score.
-Chose XGBoost for best performance.

# 6.🌐 Streamlit Web Application

-Built a web interface to collect user inputs.
-Displayed the prediction result and relevant health tips.

# 7.📄 PDF Report Generation

Used ReportLab to create a downloadable PDF of the prediction and tips.





