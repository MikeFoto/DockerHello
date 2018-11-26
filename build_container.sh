#!/usr/bin/env bash
#
# Simple aproach build container and use it locally
#
TAG=`git log -1  | cut -f 2 -d " " | head -1`
sudo docker build -t $TAG .

NAMESPACE=hellodemo
DEPLOYMENT=hellodeployment
PORT=9999
kubectl run $DEPLOYMENT \
        --image=$TAG \
        --port=$PORT
        # --image=gcr.io/hello-minikube-zero-install/hello-node \
