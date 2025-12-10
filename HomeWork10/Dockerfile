FROM nginx:alpine

ARG CURRENT_ENVIRONMENT

ENV CURRENT_ENVIRONMENT=$CURRENT_ENVIRONMENT

RUN echo "<!DOCTYPE html>" > /usr/share/nginx/html/index.html && \
    echo "<html>" >> /usr/share/nginx/html/index.html && \
    echo "<head><title>Environment Info</title></head>" >> /usr/share/nginx/html/index.html && \
    echo "<body>" >> /usr/share/nginx/html/index.html && \
    echo "<h1>Current Environment: $CURRENT_ENVIRONMENT</h1>" >> /usr/share/nginx/html/index.html && \
    echo "<p>Server is running in <strong>$CURRENT_ENVIRONMENT</strong> environment</p>" >> /usr/share/nginx/html/index.html && \
    echo "</body></html>" >> /usr/share/nginx/html/index.html

EXPOSE 80