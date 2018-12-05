from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


dataset_hostels_mach = [len(dataset[i]['hotels'].keys()) for i in dataset.keys()]

data = go.Bar(
        x= list(dataset.keys()),
        y= dataset_hostels_mach,)


fig = go.Figure(data=[data])
plotly.offline.plot(fig, filename='hotels.html')