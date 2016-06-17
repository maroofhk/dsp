import pandas as pd
from collections import Counter

df = pd.read_csv('faculty.csv')
# rename columns that have extra space in them
df.rename(columns={' degree': 'degree', ' title': 'title', ' email': 'email'}, inplace=True)
df['email'].to_csv('emails.csv', index=False)