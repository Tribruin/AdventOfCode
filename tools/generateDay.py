#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python

from datetime import datetime
from shutil import copy
import os
import sys
import subprocess
import argparse
import pytz
import requests
from TerminalColors import RED, ENDCOLOR


# Get env variables
# SESSION_ID = os.getenv("SESSIONID")

# Pulls the Session ID from One Password via the OP CLI
# Session Key is stored at Secrets/AOC2022SessionID
PasswordUUID = "oatihiwgu2syxukn2nacg3b3m4"
response = subprocess.run(
    ["op", "items", "get", PasswordUUID, "--fields", "SessionID"],
    stdout=subprocess.PIPE,
    check=True,
    text=True,
)
SESSION_ID = str(response.stdout).strip()

# Setup the directory structure
currentPath = os.path.abspath(os.path.dirname(sys.argv[0]))
parentPath = os.path.dirname(currentPath)


# currentYear = date.today().year
# currentDay = date.today().day
currentYear = datetime.now(pytz.timezone("America/New_York")).year
currentDay = datetime.now(pytz.timezone("America/New_York")).day

arg = argparse.ArgumentParser(description="Enter Year and Day if not today")
arg.add_argument("--year", type=int, default=currentYear)
arg.add_argument("--day", type=int, default=currentDay)
args = arg.parse_args()
day = args.day
year = args.year

codePath = os.path.join(parentPath, str(year), f"Day{day}")
templatePath = os.path.join(parentPath, "tools", "template")

print(f"Generating Day: {RED}{day}{ENDCOLOR} for {RED}{year}{ENDCOLOR}")

if not os.path.exists(codePath):
    print(f"    Creating path: {codePath}")
    os.makedirs(codePath)
else:
    print("    Path Already Exists")

# Copy the files the the new directory but check if the files exist
if not os.path.exists(os.path.join(codePath, "main.py")):
    print(f"    Copying main.py to {codePath}")
    copy(os.path.join(templatePath, "main.py"), os.path.join(codePath))
else:
    print(f"    main.py already exists in {codePath}")

# Create the test file
if not os.path.exists(os.path.join(codePath, f"Day{day}-Input-Test.txt")):
    print("    Creating test input file ")
    with open(
        os.path.join(codePath, f"Day{day}-Input-Test.txt"), "w", encoding="UTF-8"
    ) as f:
        f.close()
else:
    print("    Test input file already exists")

# Download the input data.

input_file = os.path.join(codePath, f"Day{day}-Input.txt")
if not os.path.exists(input_file):
    print("    Pulling Input from AOC Website")
    aoc_input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": SESSION_ID}
    headers = {"User-Agent": "github.com/tribruin by tribruin@gmail.com"}
    response = requests.get(
        url=aoc_input_url, headers=headers, cookies=cookies, timeout=10
    )
    with open(input_file, "w", encoding="UTF-8") as f:
        f.write(response.text)
else:
    print("    Input File Already Exist.")
