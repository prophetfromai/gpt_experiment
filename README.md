# FastAPI Application Deployment Guide

This README provides a comprehensive guide on how to deploy a FastAPI application using Google Cloud Build and Cloud Run. It also includes instructions on how to use **devcontainers** for local development. The guide covers commands for setting up your GCP environment, deploying the application, and ensuring proper permissions.

## Prerequisites

Before you start, ensure you have the following:
- Docker installed (for running devcontainers)
- VS Code with the **Dev Containers** extension installed
- Access to a Google Cloud project

## Devcontainer Setup

1. **Launch the Devcontainer**:
    - Open your project folder in VS Code.
    - If you have a `.devcontainer/devcontainer.json` file in your project, VS Code should prompt you to reopen the project in the container.
    - Alternatively, open the command palette (Ctrl+Shift+P) and select `Dev Containers: Reopen in Container`.

2. **Verify the Environment**:
    - Once the devcontainer is up, the Google Cloud SDK and Python should already be installed, and the environment should be ready to use. Verify by running:
      ```bash
      gcloud --version  # Confirms Google Cloud SDK is installed.
      python --version  # Verifies the Python version.
      pip list  # Lists installed Python packages.
      ```

3. **Install Dependencies**:
    - The `postCreateCommand` in your devcontainer will automatically install Python dependencies from `requirements.txt` using a virtual environment. You can verify the installation:
      ```bash
      source ./venv/bin/activate  # Activate the virtual environment.
      pip list  # Confirms that the required packages are installed.
      ```

## Setup Instructions

1. **Authenticate with Google Cloud**:
    - Since the Google Cloud SDK is already installed in the devcontainer, authenticate using:
    ```bash
    gcloud auth application-default login  # Logs in with your Google account credentials and sets them as default for the CLI.
    gcloud auth list  # Lists all the Google accounts authenticated on this machine.
    gcloud config set account zachary.gander@prophetfrom.ai  # Sets the specific account to use for the GCP CLI.
    ```

2. **Configure Google Cloud SDK**:
    ```bash
    gcloud projects list  # Lists all Google Cloud projects accessible with your account.
    gcloud config set project zac-test-1  # Sets the current working project to 'zac-test-1'.
    ```

3. **Deploy the Application**:
    - Once the project is configured, deploy the FastAPI application using Cloud Build:
    ```bash
    gcloud builds submit --config cloudbuild.yaml .  # Submits a build to Google Cloud Build using the configuration specified in 'cloudbuild.yaml'.
    ```

4. **Update Permissions**:
    - You can manually allow unauthenticated requests in the Google Cloud Console or run this command to allow public access:
      ```bash
      gcloud run services add-iam-policy-binding your-service-name \
      --member="allUsers" \
      --role="roles/run.invoker"
      ```

## Local Development with Devcontainers

1. **Run the Application Locally**:
    - Inside your devcontainer, run:
      ```bash
      uvicorn app.main:app --reload --host 0.0.0.0 --port 8080  # Starts the FastAPI server, listening on port 8080.
      ```

    - The devcontainer exposes port `8080` to your local machine, so you can access the running app by navigating to `http://localhost:8080` on your browser.

    - OR just find the start.py file and run it in VSCode. This will start the app as above from the correct folder so relative imports work. 

2. **Testing and Debugging in the Devcontainer**:
    - You can run tests and use debugging tools directly in your devcontainer. Ensure your testing framework (e.g., `pytest`) is installed:
      ```bash
      pytest  # Runs all tests in the project.
      ```

3. **Format and Lint Python Files**:
    - Navigate to the app folder and run:
    ```bash
    find . -name "*.py" -exec yapf -i {} \;  # Finds all Python files and formats them in-place using yapf.
    find . -name "*.py" | xargs pylint  # Finds all Python files and runs pylint to check for style and logic errors.
    ```

## Additional Tools and Commands

- **Dockerfile Example**:
    [Distroless Python Dockerfile Example](https://github.com/GoogleContainerTools/distroless/blob/main/examples/python3-requirements/Dockerfile)
    This link provides an example of a minimal Dockerfile for Python applications using Distroless images.

## Notes

- Ensure that you are in the correct directory and have the necessary permissions set before running the deployment commands.
- When using **devcontainers**, all dependencies and configurations should be contained within the container, ensuring consistency across environments.
