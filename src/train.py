# src/train.py

import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def load_data():
    data_path = "data/train.csv"
    df = pd.read_csv(data_path,low_memory=False)
    print("Data loaded successfully!")
    return df


def preprocess_data(df):
    # Drop unnecessary columns
    df = df.drop(columns=["ID", "Customer_ID", "SSN", "Name", "Month"])

    # Drop rows with missing values
    df = df.dropna()

    # Convert data types
    # Convert the 'Age' column to numeric, setting errors='coerce' to handle non-numeric values
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

    # Filter the DataFrame to include only rows where 'Age' is between 1 and 60
    df = df[(df["Age"] >= 1) & (df["Age"] <= 60)]

    df["Annual_Income"] = pd.to_numeric(df["Annual_Income"], errors="coerce")
    df["Monthly_Inhand_Salary"] = pd.to_numeric(
        df["Monthly_Inhand_Salary"], errors="coerce"
    )

    # Separate features and target
    X = df.drop("Credit_Score", axis=1)
    y = df["Credit_Score"]

    print("Data preprocessed successfully!")
    return X, y


def encode_data(X):
    # Identify categorical and numerical features
    categorical_features = [
        "Occupation",
        "Credit_Mix",
        "Payment_of_Min_Amount",
        "Payment_Behaviour",
        "Type_of_Loan",
    ]
    numerical_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

    # Define preprocessing steps
    numerical_transformer = SimpleImputer(strategy="median")

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numerical_transformer, numerical_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    return preprocessor


def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train, preprocessor):
    # Create a pipeline with preprocessing and model
    clf = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(n_estimators=100)),
        ]
    )

    # Train the model
    clf.fit(X_train, y_train)

    # Return the trained model
    return clf


def evaluate_model(clf, X_test, y_test):
    # Predict and evaluate
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, labels=["Poor", "Standard", "Good"])
    cm = confusion_matrix(y_test, y_pred, labels=["Poor", "Standard", "Good"])

    # Calculate AUC score
    y_test_encoded = y_test.replace({"Poor": 0, "Standard": 1, "Good": 2})
    y_pred_proba = clf.predict_proba(X_test)
    auc_score = roc_auc_score(y_test_encoded, y_pred_proba, multi_class="ovr")

    # Print metrics
    print("Model Evaluation Metrics:")
    print(f"Accuracy: {acc}")
    print(f"AUC Score: {auc_score}")
    print("Classification Report:")
    print(report)

    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.colorbar()
    tick_marks = np.arange(3)
    plt.xticks(tick_marks, ["Poor", "Standard", "Good"], rotation=45)
    plt.yticks(tick_marks, ["Poor", "Standard", "Good"])
    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    plt.tight_layout()
    cm_path = os.path.join("model", "confusion_matrix.png")
    plt.savefig(cm_path)
    print(f"Confusion matrix saved to {cm_path}")


def save_model(clf):
    model_dir = "model"
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.pkl")

    # Save the trained model
    with open(model_path, "wb") as f:
        pickle.dump(clf, f)
    print(f"Model saved to {model_path}")


def main():
    # Execute steps
    df = load_data()
    X, y = preprocess_data(df)
    preprocessor = encode_data(X)
    X_train, X_test, y_train, y_test = split_data(X, y)
    clf = train_model(X_train, y_train, preprocessor)
    evaluate_model(clf, X_test, y_test)
    save_model(clf)


if __name__ == "__main__":
    main()
