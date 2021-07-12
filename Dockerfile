FROM python:3

ADD src /src

RUN pip install --upgrade pip

CMD [ "python", "./src/StatisticsTests.py" ]