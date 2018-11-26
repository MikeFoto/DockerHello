FROM python:2
ENV PORT 6666
ENV MESSAGE "Dockerfile environment message"

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./hello.py" ]
