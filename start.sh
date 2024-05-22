#!/bin/bash

docker build -t egr0k/web-app:latest -f app/Dockerfile app/
docker push egr0k/web-app:latest
kubectl apply -f kubernetes/web-app.yaml


docker build -t egr0k/script:latest -f script/dockerfile script/
docker push egr0k/script:latest
kubectl apply -f kubernetes/script.yaml

