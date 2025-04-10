
FROM nginx:alpine

COPY ./index.html /usr/share/nginx/html/index.html
COPY ./style.css /usr/share/nginx/html/style.css

RUN apk add --no-cache curl && \
    curl -sL https://github.com/containrrr/watchtower/releases/download/v2.7.0/watchtower-2.7.0-linux-amd64 -o /usr/local/bin/watchtower && \
    chmod +x /usr/local/bin/watchtower

VOLUME /usr/share/nginx/html

EXPOSE 80

CMD ["sh", "-c", "nginx & watchtower --cleanup --interval 30"]
