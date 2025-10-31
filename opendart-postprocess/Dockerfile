FROM python:3.12

ENV DEBIAN_FRONTEND=noninteractive

# 시스템 의존성 설치 (pycairo/WeasyPrint 필요 라이브러리).
RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    libcairo2 \
    libcairo2-dev \
    pkg-config \
    fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

# pip 최신화
RUN python -m pip install --upgrade pip

# PDF 관련 Python 라이브러리 설치
RUN pip install --no-cache-dir \
    lxml \
    xhtml2pdf \
    pyhtml2pdf
    
# 작업 디렉토리
WORKDIR /app

# 기본 커맨드
CMD ["python3"]