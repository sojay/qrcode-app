FROM python:3-alpine3.18

# Install build dependencies
RUN apk add --no-cache \
    build-base \
    linux-headers \
    pcre-dev \
    python3-dev

WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
CMD python ./main.py
