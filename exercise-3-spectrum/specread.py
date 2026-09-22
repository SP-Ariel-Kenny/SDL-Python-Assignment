import csv
import scipy as sp

with open('spectrum.txt', 'r') as file:
  reader = csv.reader(file, delimiter=',')
  for row in reader:
    print(row)
