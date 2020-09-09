#!/usr/bin/env python3

import sys, glob, os, argparse
from argparse import RawTextHelpFormatter
from itertools import islice
import numpy as np

usage = "norm_plt normalizes spectra data for plots."
parser = argparse.ArgumentParser(description=usage, formatter_class=RawTextHelpFormatter)
# Log files input (Must get first to pass Job name default)
# Spectra plot arguments
parser.add_argument('-i', help='Spectra data files composed of two columns: Energy and Intensity.')
parser.add_argument('-o', help='Output file.')
parser.add_argument('-y', default=1, help='Reduce factor')
parser.add_argument('-x', default=0.0,help='X axis shift')

args = parser.parse_args()

inp_file = args.i
out_file = args.o
red_factor = int(args.y)
x_shift = float(args.x)

with open(inp_file, 'r') as inp:
    x_data = []
    y_data = []
    for line in inp:
        line = line.strip().split()
        x_data.append(float(line[0]))
        y_data.append(float(line[1]))

yred = np.amin(y_data)
y_norm = [(y-yred)/red_factor for y in y_data]
x_norm = [(x+x_shift) for x in x_data]

with open(out_file, 'w') as out:
    for i,x in enumerate(x_norm):
        out.writelines(f'{x:.2f}    {y_norm[i]:.5f}\n')