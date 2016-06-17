import pandas as pd
from collections import Counter, OrderedDict

df = pd.read_csv('faculty.csv')

# rename columns that have extra space in them
df.rename(columns={' degree': 'degree', ' title': 'title', ' email': 'email'}, inplace=True)

# ========================================================================================================

def clean_and_update_dataframe(df):
	'''
	Aim of function is to clean up dataframe columns even further. This requires one to:
	1. Make faculty degrees follow the same format and have no numeric values
	2. Generate new fields regarding seperating out the names and having a reformated one
	3. Have an abbreviated title, that is excluding the Biostatistics department from title
 	'''
	'''
	# this section of code is not was an inefficient way of updating degree column
	for index,element in enumerate(df['degree']):
		df['degree'][index] = element.strip().replace('.', '')
	'''
	df['degree'] = df['degree'].apply(lambda x: pd.Series(x.strip().replace('.', '') if x.isdigit() == False else ''))

	#seperate name into first and last name
	df['lastName'] = df['name'].apply(lambda x: pd.Series(x.split(' ')[-1]))
	df['firstName'] = df['name'].apply(lambda x: pd.Series(x.split(' ')[0]))
	df['middleName'] = df['name'].apply(lambda x: pd.Series(x.split(' ')[1] if len(x.split(' ')) == 3 else ' '))

	df['firstLastName'] = df['firstName'] + ', ' + df['lastName']
	df['abbrTitle'] = df['title'].apply(lambda x: pd.Series(x[:x.find('Professor')+len('Professor')]))

	return df

def dict_by_last_name(dFrame):
	df_updated = clean_and_update_dataframe(df)
	return {k: list(zip(g['degree'], g['abbrTitle'], g['email'])) for k,g in df_updated.groupby('lastName')}

print('--------------Dictionary by Faculty last name -----------------')
d1 = dict_by_last_name(df)
for key, val in d1.items():
	print(key, ': ', val)
print('\n')

# ========================================================================================================

def dict_by_last_and_first_name(dFrame):
	df_updated = clean_and_update_dataframe(df)

	# get relevant details, make firstLastName the index, transpose df and finally convert it to dictionary
	return df_updated[['firstLastName','degree','abbrTitle','email']].set_index('firstLastName').T.to_dict('list')

print('--------------Dictionary by Faculty (last, first) name -----------------')
d2 = dict_by_last_and_first_name(df)
for key, val in d2.items():
	print(key, ': ', val)
print('\n')


# ========================================================================================================

def sort_dict_by_last_name(converted_dict):
	return OrderedDict(sorted(converted_dict.items(), key=lambda t: t[0].split(',')[1].strip()))

print('--------------Sorted (by last name) Dictionary by Faculty (last, first) name -----------------')
d3 = sort_dict_by_last_name(d2)
for key, val in d3.items():
	print(key, ': ', val)


