import sys
import re

def greetfile(names_file, error_file):
    with open(names_file, 'r') as f:
        names = f.readlines()
    
    error_messages = []
    for name in names:
        name = name.strip()
        if not name or not name[0].islower()==False or not re.match("^[a-zA-Z]+$", name):
            error_messages.append(f"Ошибка: {name} - недопустимое имя\n")
            continue
        print(f"Nice to see u, {name}!")
    
    if error_messages:
        with open(error_file, 'w') as f:
            f.writelines(error_messages)

def greet_user():
    try:
        while True:
            name = input("Hey, what's ur name?\n")
            if name and name[0].islower()==False and re.match("^[a-zA-Z]+$", name):
                print(f"Nice to see u, {name}!")
            else:
                print("Недопустимое имя, попробуйте снова.")
    except KeyboardInterrupt:
        print("\nGoodbye!")

def main():
    if len(sys.argv) == 3:
        names_file = sys.argv[1]
        error_file = sys.argv[2]
        greetfile(names_file, error_file)
    else:
        greet_user()

if __name__ == "__main__":
    main()
