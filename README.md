# FastAPI Application Deployment Guide

This README provides a comprehensive guide on how to deploy a FastAPI application using Google Cloud Build and Cloud Run. It includes commands for setting up your GCP environment, deploying the application, and ensuring proper permissions.

## Prerequisites

Before you start, ensure you have the following:
- Google Cloud SDK installed
- Access to a Google Cloud project

## Setup Instructions

1. **Authenticate with Google Cloud**:
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
    ```bash
    gcloud builds submit --config cloudbuild.yaml .  # Submits a build to Google Cloud Build using the configuration specified in 'cloudbuild.yaml'.
    ```

4. **Update Permissions**:
    - You can manually update to allow unauthenticated requests in the Google Cloud Console or add permissions via the command line.

## Additional Tools and Commands

- **Dockerfile Example**:
    [Distroless Python Dockerfile Example](https://github.com/GoogleContainerTools/distroless/blob/main/examples/python3-requirements/Dockerfile)
    This link provides an example of a minimal Dockerfile for Python applications using Distroless images.

- **Run the Application Locally**:
    ```bash
    python -m app.main  # Runs your FastAPI application using Python's module-execution mode from the root of the project.
    ```

- **Format and Lint Python Files**:
    Navigate to the app folder and run:
    ```bash
    find . -name "*.py" -exec yapf -i {} \;  # Finds all Python files and formats them in-place using yapf.
    find . -name "*.py" | xargs pylint  # Finds all Python files and runs pylint to check for style and logic errors.
    ```

## Notes

- Ensure that you are in the correct directory and have the necessary permissions set before running the deployment commands.
- It is important to check the output of each command for errors and handle them accordingly.

