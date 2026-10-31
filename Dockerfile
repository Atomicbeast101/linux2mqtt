FROM python:3.15-alpine

# Build Arguments
ARG APP_VERSION=0.0
ENV APP_VERSION=${APP_VERSION}

# Dependencies
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Start App
WORKDIR /app
COPY requirements.txt /app
COPY bin .
COPY *.py .
COPY entrypoint.sh .
COPY setup.sh .
RUN chmod +x /app/*.sh && chown appuser:appgroup /app -R
USER appuser
ENTRYPOINT ["./entrypoint.sh"]
CMD [".venv/bin/python", "app.py"]
