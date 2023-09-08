#!/usr/bin/python3

import sys
import requests


def check_arg():
    num_arg = len(sys.argv)
    if num_arg == 1:
        print("Error: missing argument")
        sys.exit(1)
    elif num_arg > 2:
        print("Error: too many arguments")
        sys.exit(1)
    else:
        return int(sys.argv[1])

employee_id = check_arg()

url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

response = requests.get(url)

if response.status_code != 200:
    print("Error: Unable to fetch data from the API")
    sys.exit(1)

data = response.json()

total_tasks = 0
completed_tasks = 0

for task in data:
    total_tasks += 1
    if task["completed"]:
        completed_tasks += 1

print("Employee {} is done with tasks({}/{}):"
      .format(data[0]["name"], completed_tasks, total_tasks))

for task in data:
    if task["completed"]:
        print("\t {}".format(task["title"]))
