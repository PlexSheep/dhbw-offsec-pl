FROM debian:bookworm
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip python3-flask procps python3-flaskext.wtf
RUN apt-get autoremove -y
RUN yes | adduser dave
RUN mkdir /var/www
COPY var/www /var/www
COPY home/dave/ /home/dave
RUN chown www-data:www-data /var/www -R
USER dave
EXPOSE 80
WORKDIR /var/www/numfui
CMD ["python3", "/var/www/numfui/main.py"]
