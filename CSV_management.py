import pandas as pd
import csv

# read the CSV with first row as header
csv_file_instance= pd.read_csv('file_path.csv', header=[0])
csv_file_instance.head()

#print the csv read
print(csv_file_instance)

# if for example csv_file_instance. has 3 columns with user, pass and status
# iterate and print a column
for i in len(csv_file_instance):
  print(csv_file_instance['user'][i])
  
#edit a entity in the CSV file
csv_file_instance['user'][5]="Aegan@gmail.com"

#append a row to the csv
csv_file_instance = csv_file_instance.append({'user': "rs@indigo.ca",'pas':"Password",'status':"Blocked"}, ignore_index=True)

#$$$ in drop function also takes in list of entities or a string and deletes respective row or column
#delete a column in csv
csv_file_instance.drop('status', inplace=True, axis=1)
#deletea row in csv
csv_file_instance.drop(['rs@indigo.ca', inplace = True)

#save the edited instance back to csv file
csv_file_instance.to_csv('file_path.csv',index=False)
