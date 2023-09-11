#!/usr/bin/python3
"""Script that exports data in the CSV format using a REST API"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command line argument
    employee_id = sys.argv[1]
    # Validate that the employee ID is an integer
    if not employee_id.isdigit():
        print("Usage: {} <employee ID>".format(sys.argv[0]))
        sys.exit(1)
    # Make a GET request to the API endpoint for users
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    users_response = requests.get(users_url)
    # Check if the response status code is 200 (OK)
    if users_response.status_code == 200:
        # Get the JSON data from the response
        users_data = users_response.json()
        # Get the employee username from the data
        employee_username = users_data.get("username")
        # Make a GET request to the API endpoint for todos
        todos_url = "https://jsonplaceholder.typicode.com/todos"
        todos_response = requests.get(todos_url, params={"userId": employee_id})
        # Check if the response status code is 200 (OK)
        if todos_response.status_code == 200:
            # Get the JSON data from the response
            todos_data = todos_response.json()
            # Open a CSV file for writing
            file_name = "{}.csv".format(employee_id)
            with open(file_name, mode="w") as csv_file:
                # Create a CSV writer object
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                # Loop through the todos data
                for todo in todos_data:
                    # Get the task completed status and title from the data
                    task_completed_status = todo.get("completed")
                    task_title = todo.get("title")
                    # Write a row in the CSV file with the required format
                    csv_writer.writerow([employee_id, employee_username, task_completed_status, task_title])
