```bash
gcloud auth login
gcloud auth list
gcloud config set account zachary.gander@prophetfrom.ai
gcloud projects list
gcloud projects create [PROJECT_ID] --name="[PROJECT_NAME]"
gcloud config set project
gcloud config set project zac-test-1
gcloud builds submit --config cloudbuild.yaml .

# Manually update to allow unauthenticated requests in the portal or add permissions from the command line

# Reference Dockerfile
# https://github.com/GoogleContainerTools/distroless/blob/main/examples/python3-requirements/Dockerfile

# From the app folder:
find . -name "*.py" -exec yapf -i {} \;
find . -name "*.py" | xargs pylint
```