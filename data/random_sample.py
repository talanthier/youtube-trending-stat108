import pandas as pd 

raw_data = pd.read_csv('US_youtube_trending_data.csv')
data_no_desc = raw_data.drop(['description'],axis = 1) # dropping description column

sampled_data = data_no_desc.sample(frac = 0.1, random_state = 123)

sampled_data.to_csv('sampled_data.csv')
