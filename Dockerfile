FROM python:3
LABEL Maintainer="Scott-Crawshaw"
ADD tagup_api.py /
RUN pip3 install flask
CMD ["python3", "tagup_api.py"]