## OWA BruteForce

A Python script for brute forcing Outlook Web Access (OWA) logins. Supports single or multiple usernames and passwords.

### Requirements
- Python 3.x
- Unix-like operating system (tested on Ubuntu 20.04)

### Usage

1. Clone the repository:

```git clone https://github.com/ChrishSec/OWA_BruteForce.git```

2. Install the required dependencies:

```pip3 install -r requirements.txt```

3. Run the OWA BruteForce:

```
$ python3 owa_bruteforce.py -h
usage: owa_bruteforce.py [-h] -t TARGET -u USER -p PASSWORD

OWA Brute Force Attack Tool By ChrishSec.com

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target URL (e.g., webmail.target.com)
  -u USER, --user USER  Single username or file containing usernames
  -p PASSWORD, --password PASSWORD
                        Single password or file containing passwords
```

## Disclaimer

This tool is intended for educational and research purposes only. Use it at your own risk. The author is not responsible for any damage caused by the use or misuse of this tool.

## License

This tool is released under the GNU General Public License v3.0. Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

## Author

This tool was developed by [ChrishSec](https://github.com/ChrishSec). Feel free to fork, modify, and distribute it. If you have any questions or suggestions, please reach out to the author on [Telegram](https://t.me/ChrishSec).
