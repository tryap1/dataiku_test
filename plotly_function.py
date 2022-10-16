import plotly.express as px
from dataiku import insights

def plotly_3d(df, PurchaseHour, CustomerAge, OrderTotal):
    fig = px.scatter_3d(df, x = PurchaseHour, y = CustomerAge, z = OrderTotal)
    insights.save_plotly("3d_plot", fig)
