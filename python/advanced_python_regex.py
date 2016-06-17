import pandas as pd
from collections import Counter

df = pd.read_csv('faculty.csv')
# specify the column names:
print('dataframe column names: %s' % df.columns)
# rename columns that have extra space in them
df.rename(columns={' degree': 'degree', ' title': 'title', ' email': 'email'}, inplace=True)
# remove '.' from the degree specifications
for index,element in enumerate(df['degree']):
	df['degree'][index] = element.replace('.', '')

# ========================================================================================================
def types_and_freq_of_degrees(degrees):
	'''
	return the frequency of degrees held by faculty
	'''
	deg  = []
	for element in degrees:
		if not element.isdigit():
			deg.extend(element.strip().split())
	return Counter(deg)

print('type and frequency of degrees: %s' % types_and_freq_of_degrees(df['degree']))

# ========================================================================================================
def types_freq_of_titles(titles):
	'''
	returns the frequency of titles held by faculty
	'''
	title = []
	for element in titles:	
		if element.find(' is ') != -1:
			element = element.replace(' is ', ' of ')	
		title.append(element.strip())
	return Counter(title)

print(types_freq_of_titles(df['title']))

# ========================================================================================================
def email_to_list(emails):
	'''
	takes in parameter of Series of emails and converts to list
	'''
	return emails.tolist()

for element in email_to_list(df['email']):
	print(element)

# ========================================================================================================
def email_domain_list(emails):
	email_domain = []
	for email in emails:
		email_domain.append(email.strip().split('@')[1])
	return Counter(email_domain)

print(email_domain_list(df['email']))