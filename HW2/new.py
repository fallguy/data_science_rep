import csv


ATHLETES_FILE = 'hw2-athletes.csv'

athletes = []

with open(ATHLETES_FILE, 'r', encoding='UTF-8') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        try:
            row['age'] = int(row['age'])
            row['height'] = int(row['height'])
            row['weight'] = int(row['weight'])
            row['age' and 'height' and 'weight'] > 0
            athletes.append(row)
        except ValueError:
            pass