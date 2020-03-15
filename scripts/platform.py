from sys import platform
import os


if "linux" in platform:
    os.system('python linux.py')
elif "darwin" in platform:
        os.system('python darwin.py')
elif "win" in platform:
        os.system('python win.py')
else:
    print("operating system not supported")


    # os.system('sudo apt install wireguard')

    # os.system('brew install wireguard-tools')
