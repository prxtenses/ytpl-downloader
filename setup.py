import subprocess
import sys
import os, atexit
import time

def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])

def main():

    my_packages = ['pytube', 'rich']

    for package in my_packages:
        install(package)
        print("\n")

    print('Dependencias baixadas')

    time.sleep(5)

    atexit.register(lambda file = __file__: os.remove(file))

if __name__ == '__main__':
    main()