FROM python:3.7

WORKDIR /streamlit
COPY ./ /streamlit
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]
