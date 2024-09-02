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

