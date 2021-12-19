import os
import csv
import json
from datetime import datetime

lokupfile = 'Mobilephone'

with open("Mobilephones.txt")as dp:
    fr=csv.DictReader(dp,delimiter='|')

    for i in fr:
        print(i)
        
