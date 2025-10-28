# Dockerfile
FROM python:3.12-slim

# pip 최신화
RUN python -m pip install --upgrade pip

# PDF 관련 Python 라이브러리 설치 (weasyprint 제외)
RUN pip install --no-cache-dir \
    xhtml2pdf \
    pyhtml2pdf

# 작업 디렉토리
WORKDIR /app

# 기본 커맨드
CMD ["python3"]
