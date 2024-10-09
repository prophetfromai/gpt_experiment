```bash
gcloud auth login
gcloud auth list
gcloud config set account zachary.gander@prophetfrom.ai
gcloud projects list
gcloud projects create my-test-project-fastapi --name="my-test-project-fastapi"
gcloud config set project my-test-project-fastapi
gcloud builds submit --config cloudbuild.yaml .

# Manually update to allow unauthenticated requests in the portal or add permissions from the command line

# Reference Dockerfile
# https://github.com/GoogleContainerTools/distroless/blob/main/examples/python3-requirements/Dockerfile

# From the app folder:
find . -name "*.py" -exec yapf -i {} \;
find . -name "*.py" | xargs pylint
```