#!/bin/bash

# Configuration variables
DOCKER_USERNAME="switzerswish"      # Your Docker Hub username
IMAGE_NAME="ancient-futures-color-llm-app"     # Name of the Docker image
TAG="latest"                         # Tag for the Docker image

# Check if Docker is running
if ! docker info >/dev/null 2>&1; then
    echo "Docker does not seem to be running, start it first and retry"
    exit 1
fi

# Log in to Docker Hub
echo "Logging in to Docker Hub..."
docker login || { echo "Failed to log in to Docker Hub"; exit 1; }

# Build the Docker image
echo "Building Docker image ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG}..."
docker build -t ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG} . || { echo "Docker build failed"; exit 1; }

# Push the Docker image
echo "Pushing image to Docker Hub..."
docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG} || { echo "Failed to push the image"; exit 1; }

echo "Docker image has been successfully built and pushed to Docker Hub!"

