# numfui

Dave is a self-proclaimed "cool haxx0r". You have access to his new web UI for
a number formatter.

## 🚀 Setup

```bash
docker compose up
# or if you only got the docker image
docker load -i numfui-VERSION-docker.tar
docker run -dp 127.0.0.1:8000:80 numfui:VERSION
# the webservice will be available on http://localhost:8000
```

## 🏆 Flag Format

The flag is in the format: `FLAG{random_string}` (a bit obfuscated, you will
recognize it when you see it)

Good luck and happy hacking!

> [!CAUTION]
> Spoilers below

## 💡 Hints

<details>
<summary>Hint 1: Web Vulnerability</summary>
Look carefully at the way you input numbers. Perhaps you can somehow send
non-numbers to the webservice?
</details>

<details>
<summary>Hint 2: Getting Access</summary>
The Webform number field is vulnerable to os-command injection. Play around with
it a bit and use urlencoding where needed.
</details>

<details>
<summary>Hint 3: Finding the Binary</summary>
Dave mentions a program to calculate time in his notes. Check his /home/dave/.local/bin directory for a binary called "timars".
</details>

<details>
<summary>Hint 4: Parameter Exploration</summary>
The timars program has specific parameters (-f/--from, -t/--to, -p/--pause). Dave seems to have a favorite number...
</details>

<details>
<summary>Hint 5: Easter Egg</summary>
Check the web application code for any special values or preferences Dave might have. The number 1337 seems significant to him.
</details>

<details>
<summary>Hint 6: Bruteforce</summary>
Reverse engineering this rust application seems tedious. Try brute forcing the
parameters, and keep his favorite number in mind.
</details>
