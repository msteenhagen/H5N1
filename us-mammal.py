#! /usr/local/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
csv_url = "https://www.aphis.usda.gov/animal_health/data-csv/hpai-mammals.csv"
data = pd.read_csv(csv_url, parse_dates=['Date Collected', 'Date Detected'], usecols=(2,3))
data.set_index('Date Collected', inplace=True)
data = data.rename(columns={'Date Detected': 'Detections (cumulative)'})
per_day = data.resample('d').count().cumsum()                                                    
plot = per_day.plot(title='2022-2023 Detections of HPAI in Mammals in the USA',figsize=(9, 6))
source = "Source: aphis.usda.gov"
plt.figtext(0.8, 0.13, source, wrap=True, horizontalalignment='center', fontsize=9)
plot.set_ylim(0)
plot.figure.savefig('plot.png')