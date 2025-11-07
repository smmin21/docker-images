FROM python:3.11-slim

# 필수 시스템 라이브러리 + 한글 폰트 설치
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libcairo2 \
    libffi-dev \
    shared-mime-info \
    fonts-nanum \
    vim-tiny \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# WeasyPrint 설치
RUN pip install --no-cache-dir \
    weasyprint \
    lxml==6.0.1 \
    fastapi==0.121.0

WORKDIR /app
COPY . /app

CMD ["bash"]
