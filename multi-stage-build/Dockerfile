# Stage 1: Build stage
FROM python:3.9-slim as builder

# Set the working directory
WORKDIR /app

# Copy the rest of the application code.
COPY . .

# Stage 2: Final stage (Distroless)
FROM gcr.io/distroless/python3-debian11

# Set the working directory
WORKDIR /app

# Copy the application and dependencies from the build stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app /app

# Specify the command to run the application
CMD ["your_script.py"]
