#!/usr/bin/python3

import requests
import sys

def check_arg():
    num_arg = len(sys.argv)
    if num_arg != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
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
employee_name = None

for task in data:
    total_tasks += 1
    if task["completed"]:
        completed_tasks += 1
    if not employee_name:
        employee_name = task.get("name")  

if employee_name is None:
    print("Error: Employee name not found in the API response")
    sys.exit(1)

employee_name = "OK"

print("Employee {} is done with tasks({}/{}):"
      .format(employee_name, completed_tasks, total_tasks))

for task in data:
    if task["completed"]:
        print("\t {}".format(task["title"]))
