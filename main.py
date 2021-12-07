from os import path
import json
from types import SimpleNamespace
import time

# def a(a1, a2):
#   print(a1, a2)

# def b(**kwargs):
#   a(**kwargs)

# b(a1="Noe", a2=123)

with open("../../brreg_enheter_alle.json") as f:
  # data = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
  data = json.load(f)

# print(data[0].forretningsadresse)
start = time.time()
for p in data:
  if p['navn'] == "MONA ULLAH":
    print(p)
    break

print(time.time() - start)