import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
f=pd.read_csv('levels.csv')
mean = f.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
print(mean)
data1=px.scatter(mean,x='student_id',y='level',size='attempt',color='attempt')
data1.show() 