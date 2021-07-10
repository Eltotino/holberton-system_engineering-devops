#!/usr/bin/python3
"""To CSV module"""
import csv
import requests
import sys



def Csv(employee_id):
    """ export data to CSV"""
    employee_id = sys.argv[1]
    r1 = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + employee_id).json()
    employee_username = r1.get('username')
    r2 = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (employee_id) + '/todos')
    with open("{}.csv".format(employee_id), "w") as CSVFile:
        author = csv.writer(CSVFile, quoting=csv.QUOTE_ALL)
        for T in r2.json():
            author.writerow([employee_id, employee_username,
                            T.get('completed'), T.get('title')])

if __name__ == "__main__":
    Csv(sys.argv[1])
