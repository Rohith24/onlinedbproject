import os,django,sys,click,openpyxl
sys.path.append("F:\Summer\onlinedbproject")
os.environ["DJANGO_SETTINGS_MODULE"] = "onlinedbproject.settings"
django.setup()
from mrnd.models import *
from django.db.models import *
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('Rohith24','phnzi957gf')
clg_details=Mark.objects.values_list('student__college__Acronym').annotate(avg=Avg('total'),min=Min('total'),max=Max('total'))
print clg_details.query
max_data = go.Bar(x=[clg[0] for clg in clg_details],
               y=[clg[1] for clg in clg_details],name='max')
avg_data = go.Bar(x=[clg[0] for clg in clg_details],
               y=[clg[2] for clg in clg_details],name='avg')
min_data = go.Bar(x=[clg[0] for clg in clg_details],
               y=[clg[3] for clg in clg_details],name='min')
data = [max_data, avg_data,min_data]
layout = go.Layout(
    barmode='group'
)

py.offline.plot(data, filename='basic-bar')