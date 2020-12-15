import time
from api import *
from requests import get
from defaultenv import env
import argparse

def puship():
    subdomain = (env('SUBDOMAIN'))
    ip = get('https://api.ipify.org').text

    updatehost(subdomain, ip)

parser = argparse.ArgumentParser(description='DigitalOcean Dynamic DNS')
parser.add_argument("--add", nargs='+', help="Add a hostname. Syntax: '--add hostname ip'")
parser.add_argument("--update", nargs='+', help="Update a hostname. Syntax: '--update hostname ip'")
parser.add_argument("--auto", help="Auto update a hostname that specified in .env", action = 'store_true')
parser.add_argument("--delete", nargs='+', help="Delete a hostname. Syntax: '--delete hostname ip'")
args = parser.parse_args()

if args.add:
    try:
        addhost(args.add[0], args.add[1])
    except Exception as e:
        print(e)

elif args.update:
    try:
        updatehost(args.update[0], args.update[1])
    except Exception as e:
        print(e)

elif args.delete:
    try:
        delhost(args.delete[0])
    except Exception as e:
        print(e)

elif args.auto:
    try:
        puship()
    except Exception as e:
        print(e)

else:
    print ('Use: ddns.py [-h] for help')
