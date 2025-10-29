# ===========================================================
# Base: Apache Airflow Slim Image (Python 3.12)
# ===========================================================
FROM apache/airflow:slim-3.1.1-python3.12

USER root

# -----------------------------------------------------------
# System dependencies: ODBC + Kerberos + Hadoop client libs
# -----------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc \
    libkrb5-dev \
    libsasl2-modules-gssapi-mit \
    krb5-user \
    curl \
    vim \
    tar \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------------
# OpenJDK 11 설치 (tar.gz)
# -----------------------------------------------------------
COPY openjdk-11.0.2_linux-x64_bin.tar.gz /tmp/
RUN mkdir -p /usr/lib/jvm && \
    tar -xzf /tmp/openjdk-11.0.2_linux-x64_bin.tar.gz -C /usr/lib/jvm && \
    rm /tmp/openjdk-11.0.2_linux-x64_bin.tar.gz

ENV JAVA_HOME=/usr/lib/jvm/jdk-11.0.20
ENV PATH=$JAVA_HOME/bin:$PATH

# -----------------------------------------------------------
# Kerberos / Hadoop environment variables
# -----------------------------------------------------------
ENV HADOOP_CONF_DIR=/etc/hadoop/conf
ENV YARN_CONF_DIR=/etc/hadoop/conf
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

# -----------------------------------------------------------
# Cloudera ODBC drivers
# -----------------------------------------------------------
ENV LD_LIBRARY_PATH=/opt/cloudera/parcels/CDH/lib/hadoop/lib/native
ENV ODBCINI=/etc/odbc.ini
ENV ODBCSYSINI=/etc

# -----------------------------------------------------------
# Python dependencies
# -----------------------------------------------------------
USER airflow

RUN pip install --no-cache-dir \
    pyspark==3.1.1 \
    pyodbc \
    pandas \
    numpy \
    sqlalchemy


WORKDIR /opt/airflow
USER root
CMD ["bash"]