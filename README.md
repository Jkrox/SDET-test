# Introduction

A simple app to run end-to-end tests with Playwright and Pytest.

# Set up 

- Python 3.12 or higher 
- Docker (Alternative/Optional)

# Getting Started

## Running the Project with Python

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Jkrox/SDET-test.git
    cd SDET-test/
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the tests**:
    ```sh
    pytest
    ```

## Running the Project with Docker

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Jkrox/SDET-test.git
    cd SDET-test/
    ```

2. **Build the Docker image**:
    ```sh
    docker build -t wordcounter-test .
    ```

3. **Run the Docker container**:
    ```sh
    docker run --rm -v $(pwd):/app wordcounter-test
    ```

4. **View the test report**:
    Open the `report.html` file generated in the project directory.
