# glibplot
Python script that uses matplotlib to easily create plots from txt files with two columns of x and y values.

## Usage

plot needs only one or more text files containing x and y values for plot generation. It has many different options of plot
and color styles taken from *matplotlib* and its objective is to simplify the plotting of graphs in a professional way. 

The default behavior is to create a figure without any labels or title, but you can choose these parameters creating an text file
to be supplied as a command line argument with all the desired information (see the labels_format.txt and the examples).

Usage: 

> plot.py [-h] [-i I] [-o O] [-n N] [-l L] [-xi XI] [-xf XF] [-ym YM] [-c C] [-s S] [--show_colors] [--show_styles] 

All the options can be viewed using the help from the command line:

> plot.py -h 

Optional arguments: 

>-h, --help        
Show this help message and exit  

>-i                
Data files composed of two columns, x and y and separated by commas.  

>-o  
Output .png plot file.  

>-n  
Title of the picture.  

>-l  
Label file. (Leave it blank for no labels)  

>-xi  
Initial x value. (Leave it blank to take all range of values from file)  

>-xf  
Final x value. (Leave it blank to take all range of values from file)  

>-ym  
y axis maximum value. (Leave it blank for automatic selection using maximum value) 

>-c  
Color Map Style (Use plot --show_colors for options)  

>-s  
Plot Style (Available options from "matplotlib.style.available")  

>--show_colors  
Show Available Color Map Styles  

>--show_styles  
Show Available Plot Styles  
