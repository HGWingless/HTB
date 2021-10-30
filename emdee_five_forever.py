# This code has badly named variables, but it works
# 20211029 - Wingless
import hashlib
import re
import requests

pull = requests.session()
url = "http://138.68.156.206:30418"

pull_page = pull.get(url)  # Pull page
page = pull_page.content
page_convert = page.decode()  # Convert from bit to string
lines = []


def no_html(html):  # Strip HTML out of page
    crit = re.compile('<.*?>')
    return re.sub(crit, '', html)

line_parse = no_html(page_convert)
line = line_parse.split('string')[1].strip()  # Split right before MD5

hashed = hashlib.md5(line.encode()).hexdigest()  # Hash that string

data = dict(hash=hashed)  # Build POST
exploit = pull.post(url=url, data=data)  # Send POST
print(exploit.text)  # Be able to view page results

