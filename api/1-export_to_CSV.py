#!/usr/bin/python3
""" a request """
import requests
import csv
import sys

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_id = user_data['id']
    username = user_data['username']

    # Fetch todo data
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Create a CSV file with the user's tasks
    csv_file = f"{user_id}.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            task_completed = "True" if task["completed"] else "False"
            writer.writerow([user_id, username, task_completed, task["title"]])
