# Slack bulk messager
A script for powerful beings wanting to spam slack users swiftly and efficiently.
> _"With great power comes great responsibility" - Uncle Ben_

## Requirements
- [Python](https://www.python.org/downloads/). This script was tested with version 3.8.5.
- A Slack API Token (example: `xoxb-0000000000-0000000000000-AAAAAAAAAAABBBBBBBBBBBBB`) for an app with the following Oauth permissions:
```
chat:write
groups:read
im:read
incoming-webhook
mpim:read
users:read
users:read.email
```

## Install

## On a mac
Navigate to the project directory,and create a virtual environment:
```
python -m venv slacker
```

Activate the environment:
```
source slacker/bin/activate
```

Install the requirements:
```
pip install -r requirements.txt
```

When you're finished using the script just type:
```
deactivate
```

## On Windows (TO TEST)
Create a virtual environment in the project directory:
```
c:\>c:\<Python Directory>\python -m venv c:\path\to\project_directory\slacker
```

Activate the environment:
```
C:\> slacker\Scripts\activate.bat
```

Install the requirements:
```
pip install -r requirements.txt
```

When you're finished using the script just type:
```
C:\> slacker\Scripts\deactivate.bat
```

## How to use

The script takes a csv file containing a list of user emails, and a text file with some message we want to send them. It will query the Slack workspace for the user IDs matching each email, and will use that ID, to send each user the chosen message.
This is done sequentially, and with a delay (configurable with `WAIT_TIME_SECONDS`), in order to not hit any rate limiting from Slack's end.

```
usage: slacker.py [-h] [--token TOKEN] csv message
```

Example:
```
python slacker.py example_users.csv example_message.txt --token xoxb-0000000000-0000000000000-AAAAAAAAAAABBBBBBBBBBBBB
```