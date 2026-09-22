import csv
import scipy as sp

with open('spectrum.txt', 'r') as file:
  for line in file.readlines():
    line = line.strip()
    print(line)
