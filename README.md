# 🐟 NumFUI: From Web to Binary Challenge 🐟

![Challenge Category](https://img.shields.io/badge/Category-Web%20%7C%20Reverse%20Engineering-blue)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

> [!CAUTION]
> Minor spoilers below

## 🎯 Challenge Description

Dave is a self-proclaimed "cool haxx0r" who believes he's created two amazing applications:
1. A web-based number formatter that just works
2. A custom Rust binary called `timars` to securely store his password

Unfortunately for Dave, his confidence might be a bit misplaced. Can you prove him wrong by exploiting his web application and then reverse engineering his binary to extract his secret password?

> "I am so smart i made a program in which i can hide my password! Behold my smartness, now I never have to use a password manager again!" - Dave

## 🚀 Setup

To get started with this challenge, clone the repository and run:

```bash
docker compose up
```

The application will be available at: `http://localhost:8080`

## 💻 Challenge Files

- `Dockerfile` - Docker configuration for the challenge environment
- `docker-compose.yml` - Docker Compose configuration
- `var/www/numfui/` - Web application files
- `home/dave/` - Dave's personal files (mostly bloat)
- Hidden binaries in Dave's `.local/bin/` directory (you need to find these!)

## 🧩 Your Task

1. Exploit the command injection vulnerability in the web application
2. Gain shell access to the container
3. Discover and analyze the `timars` binary in Dave's `.local/bin/` directory
4. Find the right combination of parameters to reveal Dave's password

## 🔎 Skills Required

- Web application security testing
- Command injection exploitation
- Shell navigation and reconnaissance
- Analysis of Rust binaries and python/flask code
- Creative parameter exploration
- Identifying hidden hints in applications

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

## 🔍 Lore

Dave, convinced of his hacking prowess, created two applications:
1. A web application that formats numbers (but has a command injection vulnerability)
2. A time calculation tool that secretly hides his password

Dave's notes suggest that he believes Rust ("the crab programming language") makes his code impenetrable to reverse engineering. His overconfidence is your opportunity.

## 📝 Note

This challenge combines web exploitation with targeted parameter exploration. While you might be tempted to reverse engineer the Rust binary completely, the solution involves finding the correct combination of parameters to reveal the hidden flag!

This CTF is meant for educational purposes only. The techniques demonstrated should only be used in controlled environments with proper authorization.

## 🏆 Flag Format

The flag is in the format: `FLAG{random_string}` (a bit obfuscated, you will
recognize it when you see it)

Good luck and happy hacking!

---

*"It is also super duper safe since I used the crab programming language. No one will ever be able to reverse engineer it! I am so a cool haxx0r"* - Dave, moments before disaster
