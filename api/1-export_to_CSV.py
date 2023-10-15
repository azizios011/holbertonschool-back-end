#!/usr/bin/python3
import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    user_data = response.json()

    if 'id' not in user_data:
        print(f"No user found with ID {employee_id}")
        sys.exit(1)

    tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    tasks_response = requests.get(tasks_url)
    tasks = tasks_response.json()

    if not tasks:
        print(f"No tasks found for user {user_data['name']}")
        sys.exit(1)

    file_name = f'{employee_id}.csv'

    with open(file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks:
            user_id = user_data['id']
            username = user_data['username']
            task_completed = task['completed']
            task_title = task['title']

            csv_writer.writerow([user_id, username, str(task_completed), task_title])

    print(f"Data exported to {file_name}")
