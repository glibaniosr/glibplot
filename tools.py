#!/usr/bin/env python3

# Tools for plt_plot
import numpy as np

#----- Functions
def normalize(x_data, y_data, x_shift=0.0, red_factor=1):

    import numpy as np

    yred = np.amin(y_data)
    y_norm = [(y-yred)/red_factor for y in y_data]
    x_norm = [(x+x_shift) for x in x_data]

    return x_norm,y_norm


# from sklearn import preprocessing
# import numpy as np

# a = np.random.random((1, 4))
# a = a*20
# print("Data = ", a)

# # normalize the data attributes
# normalized = preprocessing.normalize(a)
# print("Normalized Data = ", normalized)
	