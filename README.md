# MLOps Podman Project with Credit Score Classifier Dataset

This project demonstrates a simplified MLOps pipeline using Podman. It uses the [Credit Score Classifier](https://www.kaggle.com/datasets/parisrohan/credit-score-classification?select=test.csv) dataset to train and serve a machine learning model.

## Prerequisites

- **Podman** installed on your system.
- **Make** installed on your system.
- **Dataset**: Place the `train.csv` file in the `data/` directory.

## Project Structure

```text-file
mlops-podman-project/
│
├── data/
│   └── train.csv                 # Credit Score dataset
|   └── test.csv
│
├── model/
│   └── model.pkl                 # Trained model will be saved here
│
├── src/
│   ├── train.py                  # Training script (now orchestrated by Dagster)
│   └── app.py                    # Prediction script (API endpoint)
│
├── Dockerfile                    # Dockerfile for the application
├── Makefile                      # Makefile to build and run the Podman container
├── requirements.txt              # Python dependencies
└── README.md                     # Documentation of the project


```



## Usage

### Build and Run the Application

To build the Podman image and run the container, execute:

```bash
make all
```
![Screenshot 2024-10-19 234014](https://github.com/user-attachments/assets/8f22ec33-610a-4367-b9a2-9cb8d6c4abda)

To view the logs and monitor the application

```bash
make logs
```
```bash
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     10.88.0.1:36886 - "POST /predict HTTP/1.1" 200 OK

```
