# Use the official Python 3.11 image which is more likely to be compatible with Python 3.12 requirements
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Install build tools for any native dependencies
RUN apk add --no-cache build-base libffi-dev openssl-dev bzip2-dev zlib-dev sqlite-dev bash

# Install pdm
RUN pip install pdm

# Copy the entire project including pdm.lock and pdm.json
COPY . .

# Install project dependencies using PDM
# Ensure the Python version is set correctly in the environment for PDM
ENV PDM_PYTHON=/usr/local/bin/python
RUN pdm install

# Command to run the app
CMD ["pdm", "run", "python", "src/claude_instructor_test/__init__.py"]

