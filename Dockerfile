FROM python:3.9
WORKDIR /source
COPY ./app/requirements.txt /source/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /source/requirements.txt
COPY . /source/app
CMD [ "uvicorn","app.main:app","--port","80","--reload"]