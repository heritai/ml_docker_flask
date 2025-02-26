# flask-paq-app: A Dockerized Flask API for Machine Learning

This repository contains a simple Flask API that leverages the "paq" Python package (a toy ML package) for performing basic classification and regression tasks. The application is containerized using Docker for easy deployment and reproducibility.


## Overview

This project contains the following components:

*   **`flsk.py`:** The main Flask application file.  It defines API endpoints for generating synthetic datasets, training simple models, and making predictions using the `paq` package.
*   **`Dockerfile`:** Contains instructions for building a Docker image for the Flask application.  It specifies the base image, copies application files, installs dependencies, and sets the command to run the application.
*   **`requirements.txt`:** Lists the Python packages required by the Flask application (e.g., `Flask`, `scikit-learn`, `numpy`, `paq-0.1.tar.gz`).
*   **`README.md`:** This file, providing an overview of the project, instructions for building and running the application, and other relevant information.
*   **`packaging/`:** A directory containing the custom-built `paq` Python package.  This is a crucial part of the application.  (See below for more details.)




## Setting up the `paq` Package

**Important:** This project relies on the `paq` package, which is included in this repository. Make sure `paq` package is structured as described above. The structure should be like that

```
packaging/         (Top-level package directory)
    paq/
        __init__.py   (Marks this directory as a Python package)
        ml_functions.py  (Your original code)
    setup.py      (Build and installation script)
```


## Setup and Installation

**1. Clone the Repository:**

```bash
git clone <your_repository_url>
cd flask-paq-app
```

**2. Create (or have) the `paq` Python Package:**

Make sure that you already create the `paq` python package and install it, or copy the package inside the same repository.

```
pip install paq
```

**3. Build the Docker Image:**

Navigate to the repository's root directory (where the `Dockerfile` is located) and run the following command to build the Docker image:

```bash
docker build -t flask-paq-app .
```

This command uses the instructions in the `Dockerfile` to create a Docker image named `flask-paq-app`.  The `.` specifies that the current directory is the build context.

**4. Run the Docker Container:**

Once the image is built, run a Docker container from it:

```bash
docker run -p 5000:5000 flask-paq-app
```

*   `docker run`:  The command to start a Docker container.
*   `-p 5000:5000`:  Maps port 5000 on your host machine to port 5000 inside the container. This allows you to access the Flask API from your browser or other tools.
*   `flask-paq-app`:  The name of the Docker image to run.



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

**2. Get the list of functions**

*   **Using `curl`:**

    ```bash
    curl http://localhost:5000/functions
    ```

    This will return a JSON response like:

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

To perform classification, you need to send a POST request to the `/classification/process` endpoint with the `n_samples` and `n_features` parameters in the request body.  Use `application/x-www-form-urlencoded` content type.

*   **Using `curl`:**

    ```bash
    curl -X POST -d "n_samples=100&n_features=5" http://localhost:5000/classification/process
    ```

    This will return a JSON response containing the statistics, error, and predictions:

    ```json
    {
      "error": "0.0737",
      "predictions": "[0.07, 0.10, 0.13, 0.15, 0.2, 0.12...]",
      "stats": "{'mean_target': '0.5', 'std_target': '0.5...}"
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

The process for regression is similar to classification, but you send the POST request to the `/regression/process` endpoint:

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

*   **Error Handling:** The API returns error messages in JSON format if something goes wrong (e.g., invalid parameters).  Check the `error` field in the response.
*   **Data Types:** The API expects `n_samples` and `n_features` to be integers.  Make sure you pass the correct data types in your requests.
*   **Port:** If you changed the port mapping in the `docker run` command (e.g., `-p 8080:5000`), adjust the URL accordingly (e.g., `http://localhost:8080`).





## Key Concepts

*   **Docker:** A platform for building, shipping, and running applications in containers.  Containers provide a consistent and isolated environment for your application.
*   **Docker Compose:** A tool for defining and managing multi-container Docker applications.  It uses a YAML file (`docker-compose.yml`) to configure the application's services, networks, and volumes.
*   **`Dockerfile`:**  A text file that contains instructions for building a Docker image.
*   **`requirements.txt`:**  A text file that lists the Python packages required by your application.
*   **Flask:** A micro web framework for Python.  It provides the tools and libraries you need to build web applications and APIs.
*   **`paq`:** Our example Machine learning Package.
*   **API Endpoints:** Specific URLs in your application that handle requests and return data.
*   **JSON (JavaScript Object Notation):** A lightweight data-interchange format that is commonly used in APIs.

