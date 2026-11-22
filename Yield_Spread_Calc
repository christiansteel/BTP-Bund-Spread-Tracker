df_DE = pd.DataFrame(DE_data['timeseries'])
df_DE = df_DE.rename(columns={"yield": "BUND 10Y"})

df_IT = pd.DataFrame(IT_data['timeseries'])
df_IT = df_IT.rename(columns={"yield": "BTP 10Y"})

df = df_DE.merge(df_IT,how='left',on='date')
df['Spread'] = ((df['BTP 10Y'] - df['BUND 10Y']) * 100).round(1)
df["date"] = pd.to_datetime(df["date"])
