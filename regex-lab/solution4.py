import re
import sys
from collections import defaultdict

def replace_variables(message):
    message = re.sub(r'\d+\.?\d*', '{NUMBER}', message)
    message = re.sub(r'\b(?:pid)?\d+\b', '{PID}', message)
    message = re.sub(r'\b(?:wn|srv)\d+\b', '{HOST}', message)
    return message

def process_logs():
    unique_patterns = defaultdict(int)  

    for line in sys.stdin:
        match = re.search(r'\{[^}]+\}(.*)', line)
        if match:
            message = match.group(1).strip()  
            pattern = replace_variables(message)
            print(pattern)
            unique_patterns[pattern] += 1

    sorted_patterns = sorted(unique_patterns.items(), key=lambda x: (-x[1], x[0]))

    for pattern, count in sorted_patterns:
        print(f"Template: {pattern} - Count: {count}")

process_logs()