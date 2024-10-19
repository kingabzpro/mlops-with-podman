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

To view the logs and monitor the application

```bash
make logs
```