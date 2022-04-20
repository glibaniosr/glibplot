#!/usr/bin/env python3

################################################################################################
######## Written by Gabriel Libânio Silva Rodrigues (Gabriel L. S. Rodrigues) ##################
################################################################################################

import argparse
from itertools import islice
import numpy as np
import pylab as plt
import matplotlib as mpl
from matplotlib.ticker import StrMethodFormatter
from cycler import cycler

def show_colors():
	### Color maps
	cmaps = [
	('Perceptually Uniform Sequential', 
	['viridis', 'plasma', 'inferno', 'magma', 'cividis']),
	('Cyclic', 
	['twilight', 'twilight_shifted', 'hsv']),
	('Qualitative', 
	['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c']),
	]
	for mp in cmaps:
		print(f'{mp[0]}:')
		print(*mp[1], sep=', ')
		print('')

def show_styles():
	### Plot styles
	styles = [
		'Solarize_Light2', '_classic_test', 'bmh', 'classic', 'dark_background', 
	'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 
	'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 
	'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 
	'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', 'tableau-colorblind10'
	]
	print(*styles, sep=', ')

def plot(**kwargs):

	#----------- PLOTTING Details --- defaults
	# Files
	data_files = kwargs["i"].strip().split(',')
	nplot = len(data_files)
	label_file = kwargs["l"]
	out_name = kwargs["o"]
	# Titles
	plot_title = kwargs["n"]
	x_title = ""
	y_title = ""
	# Data
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
	### Set PLOT definitions
	if kwargs["s"]:
		plot_style = kwargs["s"].strip()
		plt.style.use(plot_style) 
	if kwargs["c"]:
		color_style = kwargs["c"].strip()
		color_list = mpl.cm.get_cmap(color_style).colors
		if len(color_list) > 50:
			color_cycle = islice(color_list, 0, None, len(color_list)//(nplot//2))
		else:
			color_cycle = islice(color_list, 0, None )
		plt.rc('axes', prop_cycle=cycler(color=color_cycle)) 
	# Other configurations
	plt.ticklabel_format(useOffset=False) # Prevent the use of an offset
	plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}')) # 1 decimal places

	#----------- Gather data and apply x-shift
	x_shift = float(kwargs["xs"])
	for idx,inp_name in enumerate(data_files):
		x_values = []
		y_values = []
		with open(inp_name,'r') as inp:
			for line in inp:
				if line.startswith("#"):
					continue 
				x_values.append(float(line.strip().split()[0])+x_shift)
				y_values.append(float(line.strip().split()[1]))
		try:
			data_all.append([data_labels[idx], x_values, y_values])
		except:
			print("Your label file does not have the right amount of labels!")
			exit()

	# x and y limits
	x_all = np.concatenate([x[1] for x in data_all])
	y_all = np.concatenate([y[2] for y in data_all])
	x_i = min(x_all)
	x_f = max(x_all)
	y_i = min(y_all)
	y_f = max(y_all)*1.05
	if kwargs["xi"]:
		x_i = float(kwargs["xi"])
		x_f = float(kwargs["xf"])
	if kwargs["ym"]:
		y_f = float(kwargs["ym"])
	vbar = kwargs["vbar"]
	norm = kwargs["norm"]
	if norm:
		y_f = 1.0
	plt.xlim(x_i, x_f)
	plt.ylim(y_i, y_f)

	#----------- Plot the Spectras
	plt.figure(1)
	if vbar:
		x_vbar = float(kwargs["vbar"])
		plt.axvline(x=x_vbar, linestyle='--', color='black', linewidth=0.7)
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

def main():
	# Parameters
	usage = "plot uses the Python3 matplotlib to plot graphs from two column text files."
	parser = argparse.ArgumentParser(description=usage, formatter_class=argparse.RawTextHelpFormatter)
	# Log files input (Must get first to pass Job name default)
	# Spectra plot arguments
	parser.add_argument('-i', help='Data files composed of two columns, x and y.')
	parser.add_argument('-o', help='Output .png plot file.', default='plot.png')
	parser.add_argument('-n', help='Title of the picture.', default='')
	parser.add_argument('-l', help='Label file. (Leave it blank for no labels')
	parser.add_argument('-xi', help='Initial x value. (Leave it blank to take all range of values from file)')
	parser.add_argument('-xf', help='Final x value. (Leave it blank to take all range of values from file)')
	parser.add_argument('-xs', default=0.0, help='Shift x values by this amount')
	parser.add_argument('-ym', help='y axis maximum value. (Leave it blank for automatic selection using maximum value)')
	parser.add_argument('-vbar', help='add vertical bar at x value', default=None)
	parser.add_argument('-norm', action='store_true', help=f'Normalize all the data between 0 and 1')
	# Spectra format arguments
	#parser.add_argument('-i', action='store_true', help='Iteractive mode')
	parser.add_argument('-c', default='', help=f'Color Map Style (Use plt_plot --show_colors for options)')
	parser.add_argument('-s', default='', help=f'Plot Style (Available options with \"matplotlib.style.available\")')
	parser.add_argument('--show_colors', action='store_true', help=f'Show Available Color Map Styles')
	parser.add_argument('--show_styles', action='store_true', help=f'Show Available Plot Styles')

	# Pass arguments
	configs = parser.parse_args()
	configs_dic = vars(configs)

	# Show Color Maps if asked
	if configs_dic["show_colors"]:
		show_colors()
		exit(0)
	# Show Styles if asked
	if configs_dic["show_styles"]:
		show_styles()
		exit(0)

	plot(**configs_dic)

if __name__ == "__main__":
	main()