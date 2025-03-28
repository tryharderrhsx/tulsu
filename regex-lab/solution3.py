import re
from collections import defaultdict

def replace_numbers_with_star(message):
    return re.sub(r'\d+\.?\d*', '<*>', message)

def process_logs(file_path):
    unique_patterns = defaultdict(int)  

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'\{[^}]+\}(.*)', line)
            if match:
                message = match.group(1).strip() 
                pattern = replace_numbers_with_star(message)
                print(pattern)
                unique_patterns[pattern] += 1

    print(f"Количество уникальных шаблонов: {len(unique_patterns)}")

log_file_path = 'log_file.txt'

process_logs(log_file_path)