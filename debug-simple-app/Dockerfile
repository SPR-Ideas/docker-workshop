FROM python:3.8-alpine
WORKDIR app
COPY * .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["uvicorn", "main:app" ,"--host=0.0.0.0","--port=80"]
EXPOSE 80