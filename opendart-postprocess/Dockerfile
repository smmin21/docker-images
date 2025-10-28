FROM python:3.12-slim


ENV DEBIAN_FRONTEND=noninteractive


# 최소 시스템 라이브러리 설치 + vim
RUN apt-get update && apt-get install -y --no-install-recommends \
libcairo2 \
libpango-1.0-0 \
libgdk-pixbuf2.0-0 \
fonts-dejavu-core \
fonts-noto-core \
vim \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
&& pip install --no-cache-dir -r requirements.txt


WORKDIR /app
CMD ["bash"]