FROM alpine:latest

RUN apk add --no-cache python3-dev py3-pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt

COPY ./src .

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["/app/app.py"]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--debug=True"]
