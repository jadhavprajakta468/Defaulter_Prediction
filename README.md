# Attendance-Based Defaulter Prediction System

## Synopsis
This project focuses on developing a predictive system to identify student defaulters based on their attendance records using machine learning techniques, specifically employing the Random Forest classification model.

## Problem Statement
The project aims to create an efficient system for predicting student defaulters by analyzing their attendance data. The goal is to help educators identify students at risk of defaulting on academic obligations, enabling timely intervention and support.

## Introduction
The system utilizes a Random Forest classification model to predict whether a student is likely to be a defaulter based on their attendance history. By inputting the attendance data for the upcoming month, the system generates predictions for all students, aiding teachers in proactive intervention.

## Key Features
- **Random Forest Model:** Utilizes Random Forest algorithm for robust defaulter prediction.
- **Real-time Prediction:** Allows educators to input upcoming month's attendance data for instant defaulter predictions.
- **Data Integrity Check:** Ensures data accuracy by identifying missing values in the CSV file.
- **Outlier Detection:** Flags incorrect attendance entries such as attendance exceeding the total number of lectures.
- **Visualization:** Provides visual insights into defaulter rates and attendance patterns.
- **Model Comparison:** Evaluates and compares performance of Random Forest, K-Nearest Neighbors (KNN), and Logistic Regression models.

## Dataset Information
- **Attributes:**
  - `CNumber`: Unique student identifier.
  - `Name of the Student`: Name of the student.
  - `Attendance for each subject`: Attendance records for different subjects (IoT, SE, HS-OB, OE1-SC, OEI-ICCF, IOTL).
  - `Defaulter Status for Each Subject`: Indicates defaulter status for each subject.
  - `Overall Defaulter Status`: Indicates if the student is an overall defaulter (defaulter in at least 3 subjects).

## Setup Instructions
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure Python 3.x and necessary libraries are installed (numpy, pandas, scikit-learn).
4. Prepare your dataset in CSV format as described in Dataset Information.

## Usage
1. Run `main.py` to execute the system.
2. Input the attendance data for the upcoming month when prompted.
3. View the predictions generated for each student.
4. Use visualizations and reports for insights into attendance patterns and defaulter predictions.

## Contributors
- Prajakta Jadhav

# Output:


![image](https://github.com/jadhavprajakta468/Defaulter_Prediction/assets/142293126/314a4354-9514-4cd6-924a-0d43fd12636a)

![image](https://github.com/jadhavprajakta468/Defaulter_Prediction/assets/142293126/0eaaf267-240d-4622-8712-4c21be167abc)

![image](https://github.com/jadhavprajakta468/Defaulter_Prediction/assets/142293126/a310b7c0-fe8a-4945-b728-95c680fcb8f9)

![image](https://github.com/jadhavprajakta468/Defaulter_Prediction/assets/142293126/d6ab01a6-1bc2-4559-898e-413730985b13)

![image](https://github.com/jadhavprajakta468/Defaulter_Prediction/assets/142293126/0c762cab-bf48-4c8f-958f-ce6f9afcac65)


