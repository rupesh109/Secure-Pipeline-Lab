FROM python:3.12-slimobookworm
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONBUFFERED=1
RUN useradd --uid 10001 --no-create-home --shell /usr/sbin/nologin app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=app app.py .
USER 10001
EXPOSE 8000
HEALTHCHECK --interval=30s CMD \\
  python -c "import urlib.request as u;urlopen(http://127.0.0.1:8000/healthz')"
CMD ["gunicorn", "-b", "0.0.0:8000", "app:app"]
