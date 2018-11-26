#!/usr/bin/env bash
TAG=`git log -1  | cut -f 2 -d " " | head -1`
sudo docker build -t $TAG .
