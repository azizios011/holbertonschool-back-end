#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

import requests
import csv
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + "/user/{}/todos".format(employee_id)
    name_url = main_url + "/users/{}".format(employee_id)
    todo_result = requests.get(todo_url).json()
    name_result = requests.get(name_url).json()

    if not todo_result:
        print("No TODO data found for the provided employee ID.")
        sys.exit(1)

    employee_name = name_result.get("name")

    # Create a CSV file with the user ID as the filename
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todo_result:
            task_completed_status = "True" if todo["completed"] else "False"
            task_title = todo["title"]
            csv_writer.writerow([employee_id, employee_name, task_completed_status, task_title])

    # Count the tasks in the CSV
    with open(csv_filename, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        task_count = len(list(csv_reader))  # Subtract 1 for the header row

    print(f"Data exported to {csv_filename}.")
    if task_count == len(todo_result):
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Mismatch")
