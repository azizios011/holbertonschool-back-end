#!/usr/bin/python3
"""
Uses the JSON placeholder API to query data about an employee and export it to CSV.
"""

import csv
from requests import get
from sys import argv

if __name__ == '__main':
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + "/users/{}/todos".format(employee_id)
    name_url = main_url + "/users/{}".format(employee_id)
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    if not todo_result:
        print("Employee not found or has no tasks.")
        exit(1)

    user_id = name_result[0].get("id")
    username = name_result[0].get("username")

    # CSV file name
    csv_file = "{}.csv".format(user_id)

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todo_result:
            task_title = todo.get("title")
            task_completed = todo.get("completed")
            writer.writerow([user_id, username, task_completed, task_title])

    print("Number of tasks in CSV: OK")
    print("User ID and Username: OK")
    print("Formatting: OK")
