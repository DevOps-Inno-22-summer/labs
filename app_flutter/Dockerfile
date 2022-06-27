FROM httpd:2.4

RUN useradd -u 8877 ahmed

EXPOSE 8080

COPY ./build/web/ /usr/local/apache2/htdocs/

USER ahmed