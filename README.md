

# Credit Risk Scoring Application

A personal project exploring how machine learning can be applied to credit risk assessment.

The project uses loan-related data to train a classification model and provides an interactive Streamlit application where users can enter a borrower profile and receive a predicted loan outcome.

## Overview

I built this project driven by my interest in finance and curiosity about how machine learning could be applied to financial problems.

This was also my first hands-on machine learning project. I started by learning the fundamentals of machine learning, explored a loan-related dataset, and then turned the trained model into an interactive application.

## Approach

The project uses several borrower and loan-related variables:

- Age
- Annual income
- Loan amount
- Interest rate

I also created a derived feature called `loan burden`, calculated from the loan amount relative to annual income.

```python
df_penting['beban_pinjaman'] = (
    df_penting['loan_amnt'] /
    df_penting['person_income']
)
````

This feature represents the loan amount in relation to the borrower's income, since the same loan amount can represent a different burden depending on the borrower's income.

## Machine Learning Model

The project uses a **Random Forest Classifier** to predict the loan outcome.

The model is trained using the selected features and the `loan_status` target from the dataset.

## Interactive Application

The trained model is integrated into a **Streamlit** application.

Users can enter:

* Borrower age
* Annual income
* Loan amount
* Interest rate

The application then calculates the loan burden and uses the trained model to generate a predicted loan outcome.

## Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* Jupyter Notebook
* Git / GitHub
* Git LFS

## Project Structure

```text
credit-risk-scoring/
│
├── app.py
├── credit.ipynb
├── train_model.py
├── credit_risk_dataset.csv
├── data_bersih_X_baru.csv
├── data_bersih_Y_baru.csv
├── model_kredit_baru.pkl
└── README.md
```

## Running the Application

Clone the repository:

```bash
git clone https://github.com/Artadipura/credit-risk-scoring.git
cd credit-risk-scoring
```

Install the required libraries:

```bash
pip install pandas scikit-learn streamlit
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Learning

This project became my first practical experience with machine learning.

Through the project, I learned how data preparation, feature creation, model training, and application development can be connected into one workflow. It also gave me more confidence to continue learning machine learning through practical projects.

## AI Assistance

I used ChatGPT during development to help me understand machine learning concepts and clarify technical questions as I worked on the project.

```
