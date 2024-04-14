FROM public.ecr.aws/docker/library/python:3.12-bullseye

COPY requirements.txt /app/
COPY *.py /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]