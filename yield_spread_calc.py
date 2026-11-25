import pandas as pd
from data_pull import IT_data, DE_data
import numpy as np
from scipy.stats import norm

df_DE = pd.DataFrame(DE_data['timeseries'])
df_DE = df_DE.rename(columns={"yield": "BUND 10Y"})

df_IT = pd.DataFrame(IT_data['timeseries'])
df_IT = df_IT.rename(columns={"yield": "BTP 10Y"})

df = df_DE.merge(df_IT,how='left',on='date')

### yield spread calc
df['Spread'] = ((df['BTP 10Y'] - df['BUND 10Y']) * 100).round(1)
df["date"] = pd.to_datetime(df["date"])

### z-score calc
window = 60
mean = df["Spread"].rolling(window).mean()
std = df["Spread"].rolling(window).std()
df["Z-score"] = (df["Spread"] - mean) / std

### VaR calc
df['PL'] = df['Spread'].diff() * - 10000
df['gapdays'] = df['date'].diff().dt.days
df = df[df['gapdays'] <= 4]
df = df.drop(columns='gapdays')

sample = df['PL'].iloc[-250:]

hist_var = -np.percentile(sample, (1 - 0.99) * 100)

param_var = -(sample.mean() + norm.ppf(1 - 0.99) * sample.std())
