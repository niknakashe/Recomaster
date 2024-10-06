# Frontend/Dockerfile

FROM python:3.10.8

RUN mkdir -p app/frontend

COPY Frontend app/frontend

WORKDIR /app/frontend

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    libsqliteodbc \
    odbcinst \
    libodbc1

# Install Microsoft ODBC Driver for SQL Server (if you're using MS SQL Server)
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17


EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

CMD ["RecoMaster.py"]