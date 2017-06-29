__author__ = 'albertogonzalez'

'''
http://nbviewer.ipython.org/github/bokeh/bokeh-notebooks/blob/master/tutorial/01%20-%20plotting.ipynb

'''


from bokeh.charts import (
Area, Bar, BoxPlot, Donut, Dot, HeatMap, Histogram,
Horizon, Line, Scatter, Step, TimeSeries,
)


from bokeh.io import output_notebook, show
from bokeh.plotting import figure
import matplotlib


output_notebook()

# create a new plot with default tools, using figure
p = figure(plot_width=400, plot_height=400)

# add a circle renderer with a size, color, and alpha
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)

show(p) # show the results


# create a new plot (with a title) using figure
p = figure(plot_width=400, plot_height=400, title="My Line Plot")

# add a line renderer
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

show(p) # show the results



from __future__ import division
import numpy as np

# set up some data
N = 20
img = np.empty((N,N), dtype=np.uint32)
view = img.view(dtype=np.uint8).reshape((N, N, 4))
for i in range(N):
    for j in range(N):
        view[i, j, 0] = int(i/N*255) # red
        view[i, j, 1] = 158          # green
        view[i, j, 2] = int(j/N*255) # blue
        view[i, j, 3] = 255          # alpha

# create a new plot (with a fixed range) using figure
p = figure(x_range=[0,10], y_range=[0,10])

# add an RGBA image renderer
p.image_rgba(image=[img], x=[0], y=[0], dw=[10], dh=[10])

show(p) # show the results


from bokeh.charts import Scatter
from bokeh.sampledata.iris import flowers

# fill a data frame with the data of interest and create a groupby object
df = flowers[["petal_length", "petal_width", "species"]]
xyvalues = df.groupby("species")

# any of the following commented are also valid Scatter inputs
#xyvalues = pd.DataFrame(xyvalues)
#xyvalues = xyvalues.values()
#xyvalues = np.array(xyvalues.values())

TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,previewsave"

scatter = Scatter(xyvalues, tools=TOOLS, ylabel='petal_width')

show(scatter)

import pandas as pd
from bokeh.charts import Bar
from bokeh.sampledata.olympics2014 import data

df = pd.io.json.json_normalize(data['data'])

# filter by countries with at least one medal and sort
df = df[df['medals.total'] > 0]
df = df.sort("medals.total", ascending=False)

# get the countries and we group the data by medal type
countries = df.abbr.values.tolist()
gold = df['medals.gold'].astype(float).values
silver = df['medals.silver'].astype(float).values
bronze = df['medals.bronze'].astype(float).values

# build a dict containing the grouped data
medals = pd.DataFrame(dict(bronze=bronze, silver=silver, gold=gold))

bar = Bar(medals, countries, title="Stacked bars", stacked=True)

show(bar)






























