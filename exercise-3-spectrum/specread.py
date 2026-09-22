import csv
import scipy as sp

spec_list = []
with open('spectrum.txt', 'r') as file:
  reader = csv.reader(file, delimiter=',')
  for row in reader:
    spec_list.append(list(map(float, row)))
spec_list
