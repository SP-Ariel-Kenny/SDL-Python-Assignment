# first attempt by me; ignore this file in favor of Ana's task3_version1

# import relevant modules
import csv
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import sys

# compile all wavelength and flux values into a single dict item
spec_dict = {
    'Wavelength' : [],
    'Flux' : []
}

# csv version
with open('spectrum.txt', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for i in range(27):
        next(reader)
    for wavelength, flux in reader:
        spec_dict['Wavelength'].append(wavelength)
        spec_dict['Flux'].append(flux)

# pandas version
df = pd.read_csv('spectrum.txt', skiprows=26)
#print(df)

# create separate arrays from spec_dict data
wavelength_array = np.genfromtxt(np.asarray(spec_dict['Wavelength'][:]), delimiter=',')
flux_array = np.genfromtxt(np.asarray(spec_dict['Flux'][:]), delimiter=',')

# plot data
def plotter():
    fig, ax = plt.subplots(figsize=(9,5))
    ax.plot(wavelength_array, flux_array, label='Spectrum')
    ax.set_xlabel('Wavelength ($\\AA$)')
    ax.set_ylabel('Flux (ADU)')
    plt.title("Full Spectrum")
    plt.legend()
    # graphical prettiness from Ana Amaya
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
plotter()

# fit polynomial to spectrum background; include amplitude, central wavelength of peak, and FWHM of peak
# created with reference to Ana Amaya's work
def polynomial(x, m, b):
    return m * x + b

# fit Gaussian to emission line peak; include amplitude, central wavelength of peak, and FWHM of peak
# created with reference to Ana Amaya's work
def gauss(x, A, mu, sig, c0, c1):
    return (c0 + c1 * x) + A * np.exp(- (x - mu)**2 / (2 * sig**2))

# extract parameters and uncertainties from polynomial and Gaussian functions
