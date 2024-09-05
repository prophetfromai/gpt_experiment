## Compose sample application
### Python/FastAPI application

Project structure:
```
├── compose.yaml
├── Dockerfile
├── requirements.txt
├── app
    ├── main.py
    ├── __init__.py

```

[_compose.yaml_](compose.yaml)
```
services:
  api:
    build: .
    container_name: fastapi-application
    environment:
      PORT: 8080
    ports:
      - '8080:8080'
    restart: "no"

```

## Deploy with docker compose

```shell
docker-compose up -d --build
```
## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED              STATUS              PORTS                                               NAMES
7087a6e79610   5c1778a60cf8   "/start.sh"   About a minute ago   Up About a minute   80/tcp, 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   fastapi-application
```

After the application starts, navigate to `http://localhost:8080` in your web browser and you should see the following json response:
```
{
"message": "OK"
}
```

Stop and remove the containers
```
$ docker compose down
```


docker buildx build --platform linux/amd64 -t gcr.io/zac-test-app-run/fastapi-python312-app:latest --push . 
cloud run deploy fastapi-python312-app \  --image gcr.io/zac-test-app-run/fastapi-python312-app:latest \
  --platform managed \
  --region us-west2 \
  --allow-unauthenticated \
  --port 8080


or
gcloud init
gcloud builds submit --config cloudbuild.yaml .

Service Account Creation
```
gcloud projects create zac-test-app-run-1

# Fetch the current project ID from gcloud config
PROJECT_ID=$(gcloud config get-value project)

gcloud beta billing projects describe $PROJECT_ID
gcloud beta billing accounts list
gcloud beta billing projects link zac-test-app-run-1 --billing-account=01ABD0-61BB11-AAACA0

gsutil mb -p $PROJECT_ID gs://zac-test-app-run-1_cloudbuild


gcloud iam service-accounts create cloud-run-deployer \
    --display-name "Cloud Run Deployer Service Account"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:cloud-run-deployer@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/run.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:cloud-run-deployer@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountUser"


gcloud iam service-accounts create app-runtime-sa \
    --display-name "App Runtime Service Account"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:app-runtime-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/run.invoker"

# Add any other necessary roles the runtime service account needs, for example:
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:app-runtime-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.objectViewer"
```


gcloud auth application-default login
gcloud auth list
gcloud config set account zachary.gander@prophetfrom.ai
gcloud projects list
gcloud config set project
gcloud config set project zac-test-1
gcloud builds submit --config cloudbuild.yaml .

manually update to allow unauthenticated requests in the portal or add permissions from command line

https://github.com/GoogleContainerTools/distroless/blob/main/examples/python3-requirements/Dockerfile
python -m app.main
from the app folder:
find . -name "*.py" -exec yapf -i {} \;
find . -name "*.py" | xargs pylint