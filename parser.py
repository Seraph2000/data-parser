import csv
import operator
import datetime
import re
import argparse

current_dir = '/home/seraphina/Documents/TRAINING/training_2019/JOB_APPLICATIONS/bink/data-parser/'
data_source_location = current_dir + 'Mobile_Phone_Masts_01_04_2019a.csv'


# parse csv and store data in
def get_data():
    data = csv.reader(open(data_source_location), delimiter=',')
    data = [item for item in data]
    return data


# sort in ascending order by parameter
def sort_data(col_num):
    data = get_data()
    sortedlist = sorted(data, key=operator.itemgetter(col_num), reverse=False)
    return sortedlist


# fetch data based on val of param
def data_by_param(param_num, val):
    data = get_data()
    filtered_data = [item for item in data[1:] if item[param_num] == val]
    return filtered_data


# Add together a numerical column
def total(param_num, results):
    get_col_and_sum = sum([float(item[param_num]) for item in results])
    return get_col_and_sum


def count_items_in_col():
    data = get_data()[1:]
    tenants = [item[2] for item in data]
    count_items = set([(item, tenants.count(item)) for item in tenants])
    count_items = {item[0]: item[1] for item in count_items}
    return count_items


def format_date(datestr):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if re.match('(.*)-(.*)-(.*)', datestr):
        d = re.match('(.*)-(.*)-(.*)', datestr).group(1)
        day = int(d)
        month = re.match('(.*)-(.*)-(.*)', datestr).group(2)
        month = months.index(month) + 1
        if len(str(month)) == 1:
            m = '0' + str(month)
        else:
            m = str(month)
        year = re.match('(.*)-(.*)-(.*)', datestr).group(3)
        y = '20' + str(year)
        year = int(y)

        date = datetime.datetime(year, month, day)
        reformatted_date = d + '/' + m + '/' + y
        return date, reformatted_date
    else:
        date = None
        return date, None


def list_rentals(data):
    d1 = datetime.datetime(1999, 6, 1)
    d2 = datetime.datetime(2007, 8, 31)
    get_data = [item for item in data if (format_date(item[5])[0] is not None) and (format_date(item[5])[0] >= d1) and (format_date(item[5])[0] <= d2)]
    results = []
    for record in get_data:
        record[5] = format_date(record[5])[1]
        record[6] = format_date(record[6])[1]
        record[8] = format_date(record[8])[1]
        results.append(record)
    return results


data = get_data()

# 1. Read in the attached file and produce a list sorted by Current Rent in ascending order . 
# Obtain the first 5 items from the resultant list and  output to the console.
def option_one():
    sorted_data = sort_data(9)
    for item in sorted_data[:5]:
        print(item)

# 2. From the list of all mast data create new list of mast data with 
# Lease Years = 25 years.
# Output the list to the console, include all data fields.
# Output the total rent for all items in this list to the console.
def option_two():
    filtered_data = data_by_param(7, '25')
    print("There are a total of {} records which correspond to lease year = 25\n".format(len(filtered_data)))
    for item in filtered_data:
        print(item)
    altogether = total(9, filtered_data)
    print("Total rent: {}".format(altogether))


# 3. Create a dictionary containing tenant name and a count of masts for each tenant. 
# Output the dictionary to the console in a readable form.
# NOTE. Treat "Everything Everywhere Ltd" and 
# "Hutchinson3G Uk Ltd&Everything Everywhere Ltd" as separate entities.
def option_three():
    count = count_items_in_col()
    print(count)


# 4. List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007.
# Output the data to the console with dates formatted as DD/MM/YYYY.
def option_four():
    for item in list_rentals(data):
        print(item)


# comment this part out for running unit tests
# implement functions as arguments
# FUNCTION_MAP = {
#         'option_one': option_one,
#         'option_two': option_two,
#         'option_three': option_three,
#         'option_four': option_four
# }

# parser = argparse.ArgumentParser()
# parser.add_argument('command', choices=FUNCTION_MAP.keys())

# args = parser.parse_args()

# func = FUNCTION_MAP[args.command]
# func()


# format_date('14-Jan-11')
