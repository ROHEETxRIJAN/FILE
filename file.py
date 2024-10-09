import os, platform, time, sys

os.system('xdg-open ')

try:
    import requests
except ImportError:
    os.system("pip install requests")

print('\u001b[37m \x1b[38;5;196m->\033[1;97mChecking For Update...')
os.system('git pull --quiet')

bit = platform.architecture()[0]
print(f'\u001b[37m \x1b[38;5;196m->\033[1;97m{bit} Found')

time.sleep(2)

try:
    from aalu import menu
    menu()
except ImportError:
    print("Error: 'aalu' module not found.")
