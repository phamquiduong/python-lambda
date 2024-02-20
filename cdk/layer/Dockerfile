FROM public.ecr.aws/lambda/python:3.11

# Set working directory
# WORKDIR /app

# Copy requirements file and install dependencies
RUN mkdir /packages
WORKDIR /packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -t .
