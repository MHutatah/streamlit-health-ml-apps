# Streamlit App - Docker Setup

This folder contains the Docker configuration for the combined Streamlit application (BMI Calculator + Iris Classifier).

## Prerequisites

- Docker and Docker Compose installed
- The `iris_model.pkl` file in the parent directory

## Building and Running

### Option 1: Using Docker Compose (Recommended)

```bash
cd docker
docker-compose up --build
```

Then open your browser to: **http://localhost:8501**

### Option 2: Using Docker CLI

```bash
# Build the image
docker build -t streamlit-health-ml-app .

# Run the container
docker run -p 8501:8501 streamlit-health-ml-app
```

Then open your browser to: **http://localhost:8501**

## Stopping the Container

Press `Ctrl+C` in the terminal, or run:

```bash
docker-compose down
```

## File Structure

```
Week3/
├── app.py                    # Combined Streamlit application
├── iris_model.pkl            # Pre-trained Iris classifier model
├── requirements.txt          # Python dependencies
└── docker/
    ├── Dockerfile            # Docker image configuration
    ├── docker-compose.yml    # Docker Compose configuration
    ├── .dockerignore         # Files to exclude from Docker build
    └── README.md             # This file
```

## Features

- **BMI Calculator**: Calculate BMI and get health category feedback
- **Iris Classifier**: Predict Iris flower species using machine learning

Switch between apps using the sidebar navigation.
