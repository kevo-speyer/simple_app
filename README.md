# Minimal Web App
Bare minimum Flask webapp with pandas and requests

## BUILD 
docker build -t simple-app .

## START SERVICE:
docker run -d -p 5000:5000 simple-app

## STOP SERVICE:
docker ps (look at the CONTAINER_ID to stop)

docker stop <CONTAINER_ID>
