import pandas as pd 
df = pd.read_csv(
    'https://raw.githubusercontent.com/jdli28/STAT440/master/summer_mount_ginini.csv'
)

# dropping all rows with 'na'
df = df.dropna()
df.to_csv('mount_ginini_final.csv')