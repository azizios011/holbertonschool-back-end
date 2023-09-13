#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Make a GET request to retrieve employee data
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_data = response.json()

    if response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    # Make another GET request to retrieve the tasks associated with the employee
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    tasks_response = requests.get(tasks_url)
    tasks = tasks_response.json()

    # Create a CSV file with the specified format
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        
        # Write the header row
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write the task data to the CSV file
        for task in tasks:
            csv_writer.writerow([employee_id, employee_data["username"], str(task["completed"]), task["title"]])

    print(f"Data exported to {csv_filename}.")
