FROM python:3.9
WORKDIR /source
COPY ./app/requirements.txt /source/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /source/requirements.txt
COPY . /source/
CMD [ "uvicorn","app.main:app","--port","8000","--host","0.0.0.0"]