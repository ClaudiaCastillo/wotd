# The base image
FROM alpine:latest

# Install python and pip
RUN apk add --update python3

# Install Python modules
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy files required for the application
COPY .env /usr/src/app/
COPY manage.py /usr/src/app/
COPY config.py /usr/src/app/
COPY app /usr/src/app/app/

# Expose the port number of the application
EXPOSE 5000

# Run the application
CMD ["python3", "/usr/src/app/manage.py", "runserver"]
