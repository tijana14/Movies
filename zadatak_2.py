import pandas as pd

def extract_user_data(file_name):
    return pd.read_csv(file_name, encoding='latin1')

def filter_users(data, country_name):
    return data[data['country'] == country_name]

def add_new_column(data):
    data['box_office'] = pd.to_numeric(data['box_office'], errors='coerce')
    data['budget'] = pd.to_numeric(data['budget'], errors='coerce')
    data['balance'] = (data['box_office'] - data['budget'])
    return data

def remove_columns(data):
    return data.drop(['language', 'country', 'duration', 'budget', 'box_office'], axis=1)

def sort_data(data):
    return data.sort_values(by='balance', ascending=False)

def top_10(data):
    return data.iloc[:10]

def load_data(data, country_name):
    file_name = f"{country_name.replace(' ', '_')}_top_10_movies.xlsx"
    data.to_excel(file_name, index=False)

file_path = 'movies.csv'  
countries = ['USA', 'Russia', 'UK', 'South Korea']
raw_data = extract_user_data(file_path)

for country in countries:
    raw_data.pipe(filter_users, country).pipe(add_new_column).pipe(remove_columns).pipe(sort_data).pipe(top_10).pipe(load_data, country)
