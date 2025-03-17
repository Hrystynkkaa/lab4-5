FROM nginx:alpine

COPY ./index.html /usr/share/nginx/html/index.html
COPY ./style.css /usr/share/nginx/html/style.css
VOLUME /usr/share/nginx/html
EXPOSE 80
