import dataiku
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import io

def plot_3d(df, col_Hour, col_Age, col_Total, folder):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs = df[col_Hour]
    ys = df[col_Age]
    zs = df[col_Total]

    ax.set_xlabel(col_Hour)
    ax.set_ylabel(col_Age)
    ax.set_zlabel(col_Total)
    ax.set_title("US Transactions Only")

    ax.scatter(xs, ys, zs)

    folder_for_plots = dataiku.Folder(folder)

    picture = io.BytesIO()
    plt.savefig(picture, format='png')
    folder_for_plots.upload_stream("US-3D.png", picture.getvalue())

