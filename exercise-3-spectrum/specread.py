import csv
import scipy as sp

spec_list = []
with open('spectrum.txt', 'r') as file:
  reader = csv.reader(file, delimiter=',')
  for row in reader:
    wavelength, flux = row.split(',')
    spec_list.append([float(wavelength), float(flux)])
spec_list
