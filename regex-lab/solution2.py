import re

with open('log_file.txt', 'r') as file:
    for line in file:
        qwe = re.search(r'host="([^"]+)"', line)
        if qwe:
            host = qwe.group(1)
            print(host)