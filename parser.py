import csv
import sys
import operator

current_dir = '/home/seraphina/Documents/TRAINING/training_2019/JOB_APPLICATIONS/bink/data-parser/'
data_source_location = current_dir + 'Mobile_Phone_Masts_01_04_2019a.csv'


# parse csv and store data in
def get_data():
    data = csv.reader(open(data_source_location), delimiter=',')
    data = [item for item in data]
    return data


# allow user input
def user_params():
    return "Testing..."


# sort in ascending order by parameter
def sort_data(col_num):
    data = get_data()
    sortedlist = sorted(data, key=operator.itemgetter(col_num), reverse=False)
    return sortedlist


# fetch data based on val of param
def data_by_param(param_num, val):
    data = get_data()
    # or lambda?
    filtered_data = [item for item in data if data[param_num] == val]
    return filtered_data


# 1. Read in the attached file and produce a list sorted by Current Rent in ascending order . 
# Obtain the first 5 items from the resultant list and  output to the console.

sorted_data = sort_data(9)
for item in sorted_data[:5]:
    print(item)

# 2. From the list of all mast data create new list of mast data with 
# Lease Years = 25 years.
# Output the list to the console, include all data fields.
results = data_by_param(7, 25)
for item in results:
    print(item)
# Output the total rent for all items in this list to the console.

# 3. Create a dictionary containing tenant name and a count of masts for each tenant. 
# Output the dictionary to the console in a readable form.
# NOTE. Treat "Everything Everywhere Ltd" and 
# "Hutchinson3G Uk Ltd&Everything Everywhere Ltd" as separate entities.

# 4. List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007.
# Output the data to the console with dates formatted as DD/MM/YYYY.


# if __name__ == '__main__':
#     parse_csv()
