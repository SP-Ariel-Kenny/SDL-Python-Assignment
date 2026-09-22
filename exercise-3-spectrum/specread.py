import csv
import scipy as sp
import numpy as np

spec_dict = {
  'Wavelength' : [],
  'Flux' : []
}
with open('spectrum.txt', 'r') as file:
  reader = csv.DictReader(file, fieldnames=spec_dict.keys())
  for row in reader:
    if type(row.items()) is float:
      for key, value in row.items():
        spec_dict[key].append(float(value))

spec_dict
