##To do this we need libarry 'requests', installed in python via pip enve
import requests

r = requests.get('https://inland-saving.000webhostapp.com/list.html')
print(r.text) ##print r.text
