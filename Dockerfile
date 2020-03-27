FROM arm32v7/python:3
ADD . /code
WORKDIR /code

COPY . /code
RUN pip install -r requirements.txt

#COPY . /app

CMD [ "python", "app.py" ]
