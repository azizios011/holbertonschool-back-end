#!/usr/bin/python3
""" a request """
import csv
import requests
import sys

def export_tasks_to_csv(employee_id):
    """
    Export tasks of a specific employee to a CSV file.

    Args:
        employee_id (str): The ID of the employee.

    This function fetches user data and their tasks from an API and exports the task data to a CSV file.
    The CSV file is named after the user's USER_ID.
    """

    # Fetch user data from the API
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    user_data = response.json()

    if 'id' not in user_data:
        print(f"No user found with ID {employee_id}")
        sys.exit(1)

    # Fetch the tasks for the employee
    tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    tasks_response = requests.get(tasks_url)
    tasks = tasks_response.json()

    if not tasks:
        print(f"No tasks found for user {user_data['name']}")
        sys.exit(1)

    # Define the CSV file name
    file_name = f'{employee_id}.csv'

    # Create and write data to the CSV file
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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_tasks_to_csv(employee_id)
