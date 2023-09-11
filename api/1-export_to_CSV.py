#!/usr/bin/python3

import csv
import requests
import sys


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

user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
user_response = requests.get(user_url)

if user_response.status_code != 200:
    print("Error: Unable to fetch user data from the API")
    sys.exit(1)

user_data = user_response.json()
user_id = user_data["id"]
username = user_data["username"]

csv_filename = "{}.csv".format(user_id)

with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])

    for task in data:
        task_id = task["id"]
        completed = task["completed"]
        title = task["title"]
        csv_writer.writerow([user_id, username, completed, title])

print("Data exported to {}".format(csv_filename))
