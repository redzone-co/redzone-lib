FROM python:3.10-slim

# send python logs to the console
ENV PYTHONUNBUFFERED 1

# prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# add /app to the PYTHONPATH
ENV PYTHONPATH /app

# set /app path as the default directory inside the container
WORKDIR /app

# install all requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy all files into the container
COPY . /app

# expose port 8000
EXPOSE 8000
