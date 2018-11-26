# Hello World application in docker

## Requisites

### Run
* working minicube environment

### Build
* python
* docker running  


# Python

## Hello World app
Webserver at a specific port with a simple message.

### Configuration
shell variables are used
* MESSAGE : message to be displayed
* PORT : port to bind

die if they are not defined

### Usage
  ```bash
  MESSAGE="hello from demo " PORT=1344  hello.py
  ```
# Container

Basic container creation in a Dockerfile based on python 2 image.
