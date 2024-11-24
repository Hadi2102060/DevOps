
FROM python:3.12.7

WORKDIR /app

# copy and install dependency 
COPY  req.txt  req.txt
RUN pip install --upgrade pip
RUN pip install -r req.txt

COPY . .

EXPOSE 8080

CMD [ "uvicorn","main:app","--reload"]
