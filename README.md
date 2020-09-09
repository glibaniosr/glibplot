# plt_plot
Python script that uses matplotlib to easily create plots from txt files with two columns of x and y values.

## Usage

plt_plot needs only one or more text files containing x and y values for plot generation. It has many different options of plot
and color styles taken from *matplotlib* and its objective is to simplify the plotting of graphs in a professional way. 

The default behaviour is to create a figure without any labels or title, but you can chose these parameters creating an text file
to be supplied as a command line argument with all the desired information (see the labels_format.txt and the examples).

All the options can be viewed using the help from the command line:

> plt_plot.py -h
>
>usage: plt_plot.py [-h] [-i I] [-o O] [-n N] [-l L] [-xi XI] [-xf XF] [-ym YM] [-c C] [-s S] [--show_colors] [--show_styles]  
>
>plt_plot uses the Python3 matplotlib to plot graphs from two column text files.
>
>optional arguments:  
>  -h, --help     show this help message and exit  
>  -i I           Data files composed of two columns, x and y.  
>  -o O           Output .png plot file.  
>  -n N           Title of the picture.  
>  -l L           Label file. (Leave it blank for no labels)  
>  -xi XI         Initial x value. (Leave it blank to take all range of values from file)  
>  -xf XF         Final x value. (Leave it blank to take all range of values from file)  
>  -ym YM         y axis maximum value.  
>  -c C           Color Map Style (Use plt_plot --show_colors for options)  
>  -s S           Plot Style (Available options with "matplotlib.style.available")  
>  --show_colors  Show Available Color Map Styles  
>  --show_styles  Show Available Plot Styles  
