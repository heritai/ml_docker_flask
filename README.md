# 🐳 A Dockerized Flask API for Machine Learning

This repository features a simple Flask API designed to demonstrate basic machine learning tasks using `paq`, a lightweight, toy-grade ML Python package. It is fully containerized with Docker, ensuring easy deployment and consistent reproducibility across different environments.

## ✨ Overview

The project structure includes the following key components:

*   **`flsk.py`**: The core Flask application file, defining API endpoints for synthetic data generation, model training, and predictions, all leveraging the `paq` package.
*   **`Dockerfile`**: Instructions for building the Docker image. This file specifies the base image, copies application files, installs dependencies (including `paq`), and sets the command to run the application.
*   **`requirements.txt`**: Lists Python package dependencies for the Flask application, such as `Flask`, `scikit-learn`, and `numpy`. *Note: The `paq` package is installed from its local source distribution, as detailed below.*
*   **`README.md`**: This file, providing a comprehensive overview, setup instructions, and API usage examples.
*   **`packaging/`**: This directory contains the custom-built `paq` Python package's source distribution (`paq-0.1.tar.gz`). This archive is copied into the Docker image and installed during the build process.

## 📦 The `paq` Machine Learning Package

This project integrates the custom `paq` package, provided as a source distribution (`paq-0.1.tar.gz`) within the `packaging/` directory. The `Dockerfile` is specifically configured to install this package during the image build process.

The `packaging/` directory should be structured as follows:

```
packaging/
    paq-0.1.tar.gz
```

*(The `paq-0.1.tar.gz` archive typically contains the package source, structured with files such as `paq/__init__.py`, `paq/ml_functions.py`, and `setup.py`.)*

## 🚀 Setup and Installation

Follow these steps to set up and run the Dockerized Flask API locally.

### Prerequisites

Ensure [Docker](https://docs.docker.com/get-docker/) is installed on your machine.

### Steps

**1. Clone the Repository:**

First, clone this repository to your local machine:

```bash
git clone <your_repository_url>
cd flask-paq-app
```

*   *Replace `<your_repository_url>` with the actual URL of this repository.*

**2. Build the Docker Image:**

From the repository's root directory (where `Dockerfile` is located), build the Docker image. This step installs all necessary dependencies, including the `paq` package from the `packaging/` directory.

```bash
docker build -t flask-paq-app .
```

*   `docker build`: The command to build a Docker image.
*   `-t flask-paq-app`: Tags the image with the specified name (`flask-paq-app`); you can choose a different name.
*   `.`: Specifies the current directory (`.`) as the build context, where the `Dockerfile` and application files are located.

**3. Run the Docker Container:**

Once the image is built, run a Docker container from it:

```bash
docker run -p 5000:5000 flask-paq-app
```

*   `docker run`: The command to start a Docker container.
*   `-p 5000:5000`: Maps port 5000 on your host machine to port 5000 inside the container, allowing you to access the Flask API.
*   `flask-paq-app`: The name of the Docker image to run.

## 📡 Accessing the API

With the application running in a Docker container, you can access its API endpoints using `curl` (a command-line HTTP client) or Python's `requests` library.

### 1. Welcome Message (`/`)

Retrieve a welcome message to confirm the API is operational.

*   **Using `curl`:**

    ```bash
    curl http://localhost:5000/
    ```

    Expected JSON response:

    ```json
    {
      "message": "API is set up and running"
    }
    ```

*   **Using Python `requests`:**

    ```python
    import requests

    response = requests.get("http://localhost:5000/")
    print(response.json())
    ```

### 2. List Available Functions (`/functions`)

Retrieve a list of machine learning functions exposed by the `paq` package.

*   **Using `curl`:**

    ```bash
    curl http://localhost:5000/functions
    ```

    Expected JSON response (actual values may vary based on `paq` version):

    ```json
    [
        "generate",
        "get_metric",
        "learn",
        "predict",
        "target_statistics",
        "features_statistics",
        "correlation",
        "statistics",
        "print_correlations"
    ]
    ```

*   **Using Python `requests`:**

    ```python
    import requests

    response = requests.get("http://localhost:5000/functions")
    print(response.json())
    ```

### 3. Perform Classification (`/classification/process`)

Send a POST request to perform a classification task. Include `n_samples` and `n_features` in the request body, ensuring the content type is `application/x-www-form-urlencoded`.

*   **Using `curl`:**

    ```bash
    curl -X POST -d "n_samples=100&n_features=5" http://localhost:5000/classification/process
    ```

    Expected JSON response (actual values will vary):

    ```json
    {
      "error": "0.0737",
      "predictions": [0.07, 0.10, 0.13, 0.15, 0.2, 0.12],
      "stats": {"mean_target": "0.5", "std_target": "0.5"}
    }
    ```
    *Note: The `predictions` array will contain many more values, truncated here for brevity. Similarly, `stats` will contain more detailed statistics.*

*   **Using Python `requests`:**

    ```python
    import requests

    data = {"n_samples": 100, "n_features": 5}
    response = requests.post("http://localhost:5000/classification/process", data=data)
    print(response.json())
    ```

### 4. Perform Regression (`/regression/process`)

Similar to classification, send a POST request to the `/regression/process` endpoint with `n_samples` and `n_features`.

*   **Using `curl`:**

    ```bash
    curl -X POST -d "n_samples=100&n_features=5" http://localhost:5000/regression/process
    ```

    Expected JSON response (similar to classification, actual values will vary):

    ```json
    {
      "error": "0.0512",
      "predictions": [0.52, 0.61, 0.70, 0.45, 0.88, 0.33],
      "stats": {"mean_target": "10.2", "std_target": "2.1"}
    }
    ```
    *Note: The `predictions` array will contain many more values, truncated here for brevity. Similarly, `stats` will contain more detailed statistics.*

*   **Using Python `requests`:**

    ```python
    import requests

    data = {"n_samples": 100, "n_features": 5}
    response = requests.post("http://localhost:5000/regression/process", data=data)
    print(response.json())
    ```

---

### ⚠️ Important Notes:

*   **Error Handling:** The API returns structured error messages in JSON format for issues such as invalid parameters. Always check the `error` field in the response for details.
*   **Data Types:** The API expects `n_samples` and `n_features` to be integers. Ensure these parameters are correctly typed in your requests.
*   **Port Mapping:** If you modified the port mapping in the `docker run` command (e.g., `-p 8080:5000`), remember to adjust the API URL accordingly (e.g., `http://localhost:8080`).

## 🧠 Key Concepts

*   **Docker:** A platform for developing, shipping, and running applications within isolated environments called containers, ensuring consistency across various setups.
*   **`Dockerfile`:** A script containing instructions for Docker to automatically build a container image.
*   **`requirements.txt`:** A standard file listing Python package dependencies required for a project.
*   **Flask:** A lightweight and flexible Python micro web framework used for building web applications and APIs.
*   **`paq`:** The custom, example machine learning package bundled with this application for demonstration purposes.
*   **API Endpoints:** Specific URLs within an API that handle incoming requests and return structured data.
*   **JSON (JavaScript Object Notation):** A human-readable, open standard file format and data interchange format widely used for data exchange between servers and web applications.