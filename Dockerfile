FROM python:3.13

ADD cvser.py /

COPY . .

RUN python3 -m pip install pandas openpyxl requests

ENTRYPOINT ["python3", "cvser.py"]