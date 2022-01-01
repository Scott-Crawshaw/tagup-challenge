FROM python:3
ADD tagup_api.py /
RUN pip3 install flask
CMD ["python3", "tagup_api.py"]