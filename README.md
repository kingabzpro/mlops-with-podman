# MLOps Podman Project with MLflow, Prefect, and Podman Compose

This project demonstrates a complex MLOps pipeline using Podman Compose, MLflow for experiment tracking, and Prefect for workflow orchestration. It orchestrates multiple services, including the application, MLflow tracking server, and Prefect server.

## Prerequisites

- **Podman** installed on your system.
- **Podman Compose** installed (can use `podman-compose` as a drop-in replacement for `docker-compose`).
- **Make** installed on your system.

## Project Structure

```plaintext
mlops-podman-project/
│
├── data/
│   └── credit_score_data.csv     # Credit Score dataset
│
├── model/
│   └── model.pkl                 # Trained model will be saved here
│
├── src/
│   ├── train.py                  # Training script
│   ├── predict.py                # Prediction script (API endpoint)
│
├── Dockerfile                    # Dockerfile for the application
├── Makefile                      # Makefile to build and run the Podman container
├── requirements.txt              # Python dependencies
└── README.md                     # Documentation of the project

```

## Usage

### Build and Run the Application

To build the images and run all services, execute:

```bash
make