import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib notebook

gdp = pd.read_csv('canada-gdp-per-capita.csv',skiprows = 16) # ,index_col=0
health = pd.read_csv('canada-healthcare-spending.csv',skiprows = 16) # ,index_col=0
gdp = pd.merge(gdp,health, on = "date")
mortality = pd.read_csv('canada-maternal-mortality-rate.csv',skiprows = 16) # ,index_col=0
gdp = pd.merge(gdp,mortality, on = "date")
emissions = pd.read_csv('canada-carbon-co2-emissions.csv',skiprows = 16) # ,index_col=0
gdp = pd.merge(gdp,emissions, on = "date")
gdp = gdp[[" GDP Per Capita (US $)"," Per Capita (US $)"," Per 100K Live Births"," Metric Tons Per Capita"]]
gdp.columns = ["GDP","Health Spending","Maternal Mortality","Emmision"]
Axes  = pd.plotting.scatter_matrix(gdp, figsize=(8,8),diagonal='kde');
plt.suptitle('Effect of GDP per Capita to health elements')
for item in Axes.ravel():
    item.set_xticks([])
    item.set_yticks([])