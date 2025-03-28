import re

with open('log_file.txt', 'r') as file:
    for line in file:
        if re.match(r'^2023-01-\d{2}T\d{2}:\d{2}:\d{2}Z\s+\{filename="[^"]+"\}\s+[A-Za-z]{3}\s[A-Za-z]{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}\s[A-Z]{3}\s\d{4}\sLast\supdate\slog$', line):
            print(line)