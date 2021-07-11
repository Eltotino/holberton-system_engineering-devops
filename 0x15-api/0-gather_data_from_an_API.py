#!/usr/bin/python3
"""DataAPI module"""
import requests
import sys

def APIdata(employee_id):
    """ Displays information about the ID number"""
    employee_id = sys.argv[1]
    Done = 0
    TasksDone = []
    all_tasks = 0
    user_url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
    r1 = requests.get(user_url).json()
    employee_name = r1.get('name')
    r2 = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    for i in r2:
        if i.get('userId') == int(employee_id):
            if i.get('completed'):
                TasksDone.append(i['title'])
                Done += 1
                all_tasks += 1
    print('Employee {} is done with tasks({}/{}):'.
          format(employee_name, Done, all_tasks))
    for t in TasksDone:
        print("\t {}".format(t))

if __name__ == "__main__":
    APIdata(sys.argv[1])
