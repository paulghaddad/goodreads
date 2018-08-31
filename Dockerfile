# Use Postgres runtime as parent image
FROM postgres:10.5

# Set working directory
WORKDIR /app

# Copy current directory contents to working directory
ADD . /app

# Define environment variables
ENV POSTGRES_PASSWORD ilovepostgres
