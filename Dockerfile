FROM debian:bookworm
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y openssh-server vim
# RUN systemctl enable ssh --now
RUN apt-get autoremove -y
RUN yes | adduser dave
RUN yes TESTPASS | passwd dave
COPY var/* /var
COPY home/dave/* /home/dave
CMD journalctl -f

