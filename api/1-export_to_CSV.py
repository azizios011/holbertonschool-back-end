#!/usr/bin/python3


import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"

def user_info(id):
    total_tasks = 0

    # Fetch tasks associated with the user
    response = requests.get(todos_url).json()
    for task in response:
        if task['userId'] == id:
            total_tasks += 1

    num_lines = 0
    with open(str(id) + ".csv", 'r') as f:
        for line in f:
            if not line.strip():  # Ignore empty lines
                continue
            num_lines += 1

    if total_tasks == num_lines:
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")

if __name__ == "__main__":
    user_info(int(sys.argv[1]))
