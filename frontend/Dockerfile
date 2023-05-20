FROM python:3.9
WORKDIR /frontend
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD [ "streamlit","run","homepage.py"]