FROM debian:bookworm
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip python3-flask procps
RUN apt-get autoremove -y
RUN yes | adduser dave
RUN yes TESTPASS | passwd dave
RUN mkdir /var/www
COPY var/www /var/www
COPY home/dave/* /home/dave
RUN chown www-data:www-data /var/www -R
USER dave
EXPOSE 80 22
# CMD tail -f /dev/null
CMD ["python3", "/var/www/amazing-time-calculator/main.py"]
