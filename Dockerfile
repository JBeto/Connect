FROM python:3.8

WORKDIR /vat-chan
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY vat/ vat/

# command to run on container start
ENTRYPOINT ["python3", "-m", "vat"]