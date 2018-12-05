from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go

dataset_hostels_mach = [len(dataset[i]['hotels'].keys()) for i in dataset.keys()]



#Вивести кругову діаграму: якого товару на яку суму продано.


diagram = go.Pie(labels=list(dataset.keys()), values=dataset_hostels_mach)



plotly.offline.plot([diagram], filename='hotelsdia.html')
