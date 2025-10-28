FROM python:3.12-slim

# 시스템 의존성 설치 (pycairo/WeasyPrint 필요 라이브러리)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2 \
    libcairo2-dev \
    libpango-1.0-0 \
    libpango1.0-dev \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    pkg-config \
    fonts-dejavu \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# pip 최신화
RUN python -m pip install --upgrade pip

# PDF 관련 Python 라이브러리 설치
RUN pip install --no-cache-dir \
    xhtml2pdf \
    pyhtml2pdf
    
# 작업 디렉토리
WORKDIR /app

# 기본 커맨드
CMD ["python3"]
