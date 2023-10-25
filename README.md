# Credit Card Fault Detection System

**Project Name:** Credit Card Fault/Fraud Detection System  
**Developer:** Anurag Gupta  
**Version:** 0.0.1  
**Date:** October 25, 2023

---

## Project Description

Credit Card Fraud Detection System is an end-to-end machine learning project that aims to detect fraudulent credit card transactions. This project is developed by Anurag Gupta, and provides a comprehensive solution for identifying potentially fraudulent activities in credit card transactions. The system utilizes machine learning algorithms to analyze patterns and detect anomalies in transaction data.

---

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**
    ```
    git clone https://github.com/guptaanurag2803/Credit-Card-Fault-Detection.git
    cd credit-card-fraud-detection
    ```

2. **Install dependencies:**
    ```
    python setup.py install
    ```

---

## Training the Model

To train the machine learning model, run the following command:

```
python src/pipelines/training_pipeline.py
```

This command will initiate the training process and create a model based on the provided dataset.

---

## Running the Application

To run the application, execute the following command:

```
python app.py
```

Once the application is running, you can access the prediction service through the following URL:
Homepage: http://127.0.0.1:5000/
Prediction Page: http://127.0.0.1:5000/predict

---


## Notes

- Ensure that you have Python installed on your system before running the setup and training commands.
- Make sure to provide valid and meaningful transaction data in the request body when testing the prediction endpoint.

---