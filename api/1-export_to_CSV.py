#!/usr/bin/python3
""" a request """
import csv
import requests
import sys

def export_tasks_to_csv(employee_id):
    # ... (previous code)

    # Create and write data to the CSV file
    with open(file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        task_count = 0  # Initialize the task count

        for task in tasks:
            user_id = user_data['id']
            username = user_data['username']
            task_completed = task['completed']
            task_title = task['title']

            csv_writer.writerow([user_id, username, str(task_completed), task_title])
            task_count += 1  # Increment the task count for each task

    print(f"Data exported to {file_name}")
    return task_count  # Return the task count

if __name__ == '__main':
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    exported_task_count = export_tasks_to_csv(employee_id)

    # Expected number of tasks
    expected_task_count = 20  # Set your expected task count here

    print(f"Number of tasks in CSV: {'OK' if exported_task_count == expected_task_count else 'Mismatch'}")
