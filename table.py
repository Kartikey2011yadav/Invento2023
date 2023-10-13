from json2html import *
input = []
f = open("savedata.json", "r")
input = f.read()
print(json2html.convert(json = input))