FROM alpine:latest

LABEL Owner="rahulmittal1005@gmail.com" version=1.0

COPY components /components
COPY app.py /app.py
RUN apk add --update --no-cache python3 py3-pip && \
    pip3 install flask 

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
EXPOSE 5000

ENTRYPOINT [ "python3", "/app.py" ]
