import pandas as pd 

def extract_user_data(file_name):
    return pd.read_csv(file_name, encoding='latin1') 

def filter_users(data, country_name):
    mask = (data['country'] == 'country_name')
    return data[mask]

def add_new_column(data):
    data['box_office'] = pd.to_numeric(data['box_office'], errors='coerce')
    data['budget'] = pd.to_numeric(data['budget'], errors='coerce')
    data["balance"] = data['box_office'] - data['budget']
    return data

def remove_columns(data):
    data = data.drop(['language', 'country', 'duration', 'budget', 'box_office'], axis=1)
    return data

def sort_data(data):
    return data.sort_values(by='balance', ascending=False)

def top_10(data):
    return data.iloc[:10]

def save_to_excel(data, country_name):
    file_name = f"top10_{country_name.replace(' ', '_')}.xlsx"
    data.to_excel(file_name, index=False)

file_path = 'movies.csv'
countries = ['USA', 'Russia', 'UK', 'South Korea']
raw_data = extract_user_data('movies.csv')

for country in countries:
    processed = (
        filter_users(raw_data, country)
        .pipe(add_new_column)
        .pipe(remove_columns)
        .pipe(sort_data)
        .pipe(top_10)
    )
    save_to_excel(processed, country)

#def load_data(data, filename):
    #data.to_excel(filename, index=False)
    
#countries = ['USA','Russia','UK','South Korea']

#def process_for_country(file_name, country_name, output_file):
    #df = (
        #extract_user_data(file_name)
        #.pipe(df=[df['country'] == country_name])
        #.pipe(add_new_column)
        #.pipe(remove_columns)
        #.pipe(sort_data)
         #.pipe(top_10)
    #)
    #load_data(df, output_file)
    
#countries = ['USA', 'UK', 'Russia', 'South Korea']

#for country in countries:
 #   def read_file(file_name):
  #      return pd.read_csv(file_name)

#for country in countries:
    #def read_file(file_name):
        #return pd.read_csv(file_name)

#def load_data(data):
    #data.to_excel("Top10russia.xlsx", index=False)
    
#def load_data(data):
    #data.to_excel("Top10USA.xlsx", index=False)
    
#def load_data(data):
    #data.to_excel("Top10UK.xlsx", index=False)
    
#def load_data(data):
 #   data.to_excel(country+"_movies.xlsx", index=False)
   
    
#df = extract_user_data('file_name.xlsx').pipe(filter_users).pipe(add_new_column).pipe(remove_columns).pipe(sort_data).pipe(top_10).pipe(load_data)






