### TO BUILD DOCKER IMAGE

```sh
docker build -t <IMAGE_NAME> .
```

### Execute Docker Image as a Container

```sh
docker run -d -p 8000:8000 --name <YOUR_CONTAINER_NAME> <IMAGE_NAME>
```