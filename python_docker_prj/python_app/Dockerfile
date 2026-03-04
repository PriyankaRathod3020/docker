#Get a base image of python
FROM python:3.13.12-slim

#Create a working directory inside a container
WORKDIR /app

#Install required packages for the system
RUN apt-get update \
    && apt-get upgrade -y

#Copy requirements.txt file from local machine to docker container
COPY requirements.txt .

#Install the python dependency.
#--no-cache-dir: used with  command within a Linux-based Dockerfile to prevent pip from saving downloaded packages to a local cache. This significantly reduces the size of your final Docker image. 
RUN pip install --no-cache-dir -r requirements.txt

#Copy the entire code from local machine to docker container
COPY . .

#Exposing the port nuumber. By exposing the port number we can access the container internally or between containers.
EXPOSE 5000

#Run the python app
CMD ["python3", "app.py"]
