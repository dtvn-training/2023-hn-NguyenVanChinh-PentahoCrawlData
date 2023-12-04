import csv

from selectorlib import Extractor, Formatter
import requests
from pprint import pprint
import re

# formatter = Formatter.get_all()
extractor = Extractor.from_yaml_file('./product.yml')
r = requests.get('https://www.alibaba.com/premium/shoes.html?src=sem_ggl&field=UG&from=sem_ggl&cmpgn=20794789804&adgrp=159728817030&fditm=&tgt=kwd-11020611&locintrst=&locphyscl=1028580&mtchtyp=b&ntwrk=g&device=c&dvcmdl=&creative=681548013252&plcmnt=&plcmntcat=&aceid=&position=&gad_source=1&gclid=EAIaIQobChMI2pjj_O3tggMVZAt7Bx1LlgxbEAAYAyAAEgIIj_D_BwE&tagScene=search&tagScene=search')

data = extractor.extract(r.text)
data = data['product']

fieldName = data[0].keys()

csv_file_path = 'data.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldName, delimiter=';')

    writer.writeheader()

    writer.writerows(data)