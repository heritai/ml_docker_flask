# A Dockerized Flask API for Machine Learning

This repository contains a simple Flask API that leverages the "paq" Python package (a toy ML package) for performing basic classification and regression tasks. The application is containerized using Docker for easy deployment and reproducibility.

## Overview

This repository includes the following key components and structure:

*   **`flsk.py`:** The main Flask application file. It defines API endpoints for generating synthetic datasets, training simple models, and making predictions using the `paq` package.
*   **`Dockerfile`:** Contains instructions for building a Docker image for the Flask application. It specifies the base image, copies application files, installs dependencies (including `paq`), and sets the command to run the application.
*   **`requirements.txt`:** Lists the Python packages required by the Flask application (e.g., `Flask`, `scikit-learn`, `numpy`). Note that `paq` is installed from its local distribution file, as detailed below.
*   **`README.md`:** This file, providing an overview of the project, instructions for building and running the application, and other relevant information.
*   **`packaging/`:** A directory containing the custom-built `paq` Python package's source distribution (`paq-0.1.tar.gz`). This file is copied into the Docker image and installed during the build process.

## The `paq` Machine Learning Package

This project relies on the custom-built `paq` package, which is included in this repository as a source distribution (`paq-0.1.tar.gz`) within the `packaging/` directory. The `Dockerfile` is configured to install this package as part of the Docker image build.

The `packaging/` directory structure for `paq` is typically as follows:

```
packaging/                 (Top-level package distribution directory)
    paq-0.1.tar.gz         (The compressed source distribution of paq)
```

(Inside the `paq-0.1.tar.gz` archive, you would find the package source, typically like `paq/__init__.py`, `paq/ml_functions.py`, and `setup.py`.)

## Setup and Installation

Follow these steps to get the Dockerized Flask API up and running:

**1. Clone the Repository:**

Start by cloning the repository to your local machine:

```bash
git clone <your_repository_url>
cd flask-paq-app
```

**2. Build the Docker Image:**

Navigate to the repository's root directory (where the `Dockerfile` is located) and run the following command to build the Docker image. This process will install all necessary dependencies, including the `paq` package from the `packaging/` directory.

```bash
docker build -t flask-paq-app .
```

*   `docker build`: The command to build a Docker image.
*   `-t flask-paq-app`: Tags the image with the name `flask-paq-app` (you can choose a different name).
*   `.`: Specifies that the current directory is the build context, where the `Dockerfile` and application files are located.

**3. Run the Docker Container:**

Once the image is built, run a Docker container from it:

```bash
docker run -p 5000:5000 flask-paq-app
```

*   `docker run`: The command to start a Docker container.
*   `-p 5000:5000`: Maps port 5000 on your host machine to port 5000 inside the container. This allows you to access the Flask API from your host machine's browser or other tools.
*   `flask-paq-app`: The name of the Docker image to run.

## Accessing the API (After Running the Docker Container)

Now that the application is running inside a Docker container, you can access the API endpoints using various tools. Here are some examples using `curl` (a command-line tool for making HTTP requests) and Python's `requests` library:

**1. Get the Welcome Message:**

*   **Using `curl`:**

    ```bash
    curl http://localhost:5000/
    ```

    This will return a JSON response like:

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

**2. Get the List of Available Functions:**

*   **Using `curl`:**

    ```bash
    curl http://localhost:5000/functions
    ```

    This will return a JSON response listing the functions exposed by the `paq` package:

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

**3. Perform Classification:**

To perform classification, send a POST request to the `/classification/process` endpoint with the `n_samples` and `n_features` parameters in the request body. Ensure the content type is `application/x-www-form-urlencoded`.

*   **Using `curl`:**

    ```bash
    curl -X POST -d "n_samples=100&n_features=5" http://localhost:5000/classification/process
    ```

    This will return a JSON response containing statistics, the classification error, and predictions:

    ```json
    {
      "error": "0.0737",
      "predictions": "[0.07, 0.10, 0.13, 0.15, 0.2, 0.12...]",
      "stats": "{'mean_target': '0.5', 'std_target': '0.5'...}"
    }
    ```

*   **Using Python `requests`:**

    ```python
    import requests

    data = {"n_samples": 100, "n_features": 5}
    response = requests.post("http://localhost:5000/classification/process", data=data)
    print(response.json())
    ```

**4. Perform Regression:**

The process for regression is similar to classification, but you send the POST request to the `/regression/process` endpoint.

*   **Using `curl`:**

    ```bash
    curl -X POST -d "n_samples=100&n_features=5" http://localhost:5000/regression/process
    ```

*   **Using Python `requests`:**

    ```python
    import requests

    data = {"n_samples": 100, "n_features": 5}
    response = requests.post("http://localhost:5000/regression/process", data=data)
    print(response.json())
    ```

**Important Notes:**

*   **Error Handling:** The API returns error messages in JSON format if something goes wrong (e.g., invalid parameters). Check the `error` field in the response.
*   **Data Types:** The API expects `n_samples` and `n_features` to be integers. Make sure you pass the correct data types in your requests.
*   **Port:** If you changed the port mapping in the `docker run` command (e.g., `-p 8080:5000`), adjust the URL accordingly (e.g., `http://localhost:8080`).

## Key Concepts

*   **Docker:** A platform for building, shipping, and running applications in containers. Containers provide a consistent and isolated environment for your application.
*   **`Dockerfile`:** A text file that contains instructions for building a Docker image.
*   **`requirements.txt`:** A text file that lists the Python packages required by your application.
*   **Flask:** A micro web framework for Python. It provides the tools and libraries you need to build web applications and APIs.
*   **`paq`:** Our example machine learning package, bundled with the application.
*   **API Endpoints:** Specific URLs in your application that handle requests and return data.
*   **JSON (JavaScript Object Notation):** A lightweight data-interchange format that is commonly used in APIs.