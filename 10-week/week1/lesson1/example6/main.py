import pandas as pd
import io
import requests
import matplotlib.pyplot as plt

# define the url where we will get the iris data set CSV
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# request the content
data=requests.get(url).content

# parse the CSV with pandas
cols = ['f1', 'f2', 'f3', 'f4', 'species']
iris_df=pd.read_csv(io.StringIO(data.decode('utf-8')), names=cols)

# create histograms for each numerical column
iris_df[cols[:-1]].hist()
plt.show()
