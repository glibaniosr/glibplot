#!/usr/bin/env python3

################################################################################################
######## Written by Gabriel Libânio Silva Rodrigues (Gabriel L. S. Rodrigues) ##################
################################################################################################

import sys, glob, os, argparse
from argparse import RawTextHelpFormatter
from itertools import islice
#from glibpy.general import cd
import numpy as np
import pylab as plt
import matplotlib as mpl
from cycler import *

#----- Functions
### Color maps
cmaps = [
    ('Perceptually Uniform Sequential', [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis']),
         ('Cyclic', ['twilight', 'twilight_shifted', 'hsv']),
         ('Qualitative', [
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c']),
]
### Plot styles
styles = [
    'Solarize_Light2', '_classic_test', 'bmh', 'classic', 'dark_background', 
'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 
'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 
'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 
'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', 'tableau-colorblind10'
]

# Parameters
usage = "plt_plot uses the Python3 matplotlib to plot graphs from two column text files."
parser = argparse.ArgumentParser(description=usage, formatter_class=RawTextHelpFormatter)
# Log files input (Must get first to pass Job name default)
# Spectra plot arguments
parser.add_argument('-i', help='Data files composed of two columns, x and y.')
parser.add_argument('-o', help='Output .png plot file.', default='plot.png')
parser.add_argument('-n', help='Title of the picture.', default='')
parser.add_argument('-l', help='Label file. (Leave it blank for no labels')
parser.add_argument('-xi', help='Initial x value. (Leave it blank to take all range of values from file)')
parser.add_argument('-xf', help='Final x value. (Leave it blank to take all range of values from file)')
parser.add_argument('-ym', help='y axis maximum value.')
# Spectra format arguments
#parser.add_argument('-i', action='store_true', help='Iteractive mode')
parser.add_argument('-c', default='twilight', help=f'Color Map Style (Use plt_plot --show_colors for options)')
parser.add_argument('-s', default='classic', help=f'Plot Style (Available options with \"matplotlib.style.available\")')
parser.add_argument('--show_colors', action='store_true', help=f'Show Available Color Map Styles')
parser.add_argument('--show_styles', action='store_true', help=f'Show Available Plot Styles')
args = parser.parse_args()

# Show Color Maps
show_cor = args.show_colors
if show_cor:
    for mp in cmaps:
        print(f'{mp[0]}:')
        print(*mp[1], sep=', ')
        print('')
    exit(0)
# Show Styles
show_sty = args.show_styles
if show_sty:
    print(*styles, sep=', ')
    exit(0)

#----------- PLOTTING Details
#### Files
data_files = args.i.strip().split(',')
nplot = len(data_files)
label_file = args.l
out_name = args.o
# Names
plot_title = args.n
x_title = ""
y_title = ""
data_labels = [""]*nplot
data_all = []
#---- Get plot label details on labels file if specified
if label_file:
	with open(label_file, 'r') as inp:
			for line in inp:
				data = line.split()
				if not line.startswith("#"):
					if line.startswith("plot_title"):
						plot_title = " ".join(data[2:])
					elif line.startswith("x_title"):
						x_title = " ".join(data[2:])
					elif line.startswith("y_title"):
						y_title = " ".join(data[2:])
					elif line.startswith("data_labels"):
						line = line.replace("data_labels =","")
						data_labels = line.split(",")

#----------- Plot style, colors and aesthetics
# Get definitions
plot_style = args.s.strip()
color_style = args.c.strip()
color_list = mpl.cm.get_cmap(color_style).colors
if len(color_list) > 25:
    color_cycle = islice(color_list, 0, None, len(color_list)//nplot)
else:
    color_cycle = islice(color_list, 0, None )
### Set PLOT definitions
plt.style.use(plot_style) 
plt.rc('axes', prop_cycle=cycler(color=color_cycle)) 
#mpl.rc('image', cmap=color_style)

#----------- Gather data

for idx,inp_name in enumerate(data_files):
	x_values = []
	y_values = []
	with open(inp_name,'r') as inp:
		for line in inp:
			if line.startswith("#"):
				continue 
			x_values.append(float(line.strip().split()[0]))
			y_values.append(float(line.strip().split()[1]))
	data_all.append([data_labels[idx], x_values, y_values])

# x and y limits
x_i = min(x_values)
x_f = max(x_values)
y_i = min(y_values)
y_f = max(y_values)*1.2
if args.xi:
	x_i = float(args.xi)
	x_f = float(args.xf)
if args.ym:
	y_f = float(args.ym)
plt.xlim(x_i, x_f)
plt.ylim(y_i, y_f)

#----------- Plot the Spectras
plt.figure(1)
for spec_data in data_all:
	sub = spec_data[0]
	x_data = spec_data[1]
	y_data = spec_data[2]
	plt.plot(x_data, y_data, label=(sub))
	plt.title(plot_title)
	plt.xlabel(x_title)
	plt.ylabel(y_title)
	plt.legend(prop={'size':8}, loc = 'best')
plt.savefig(out_name, dpi=160)
plt.close()

