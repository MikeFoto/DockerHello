# Hello World application in docker

## Requisites
As this is just a demo:
* no workflow or integration with remote services is coded;
* not discussed cluster access nor permissions (user/namespaces/....).

### Run
* working minikube environment access

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
