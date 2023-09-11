#!/usr/bin/python3

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
    users_url = "https://jsonplaceholder.typicode.com/users/{}"
    .format(employee_id)

    users_response = requests.get(users_url)
    # Check if the response status code is 200 (OK)
    if users_response.status_code == 200:
        # Get the JSON data from the response
        users_data = users_response.json()
        # Get the employee name from the data
        employee_name = users_data.get("name")
        # Make a GET request to the API endpoint for todos
        todos_url = "https://jsonplaceholder.typicode.com/todos"
        todos_response = requests.get
        (todos_url, params={"userId": employee_id})
        # Check if the response status code is 200 (OK)
        if todos_response.status_code == 200:
            # Get the JSON data from the response
            todos_data = todos_response.json()
            # Initialize variables to store the total number
            # of tasks and the number of done tasks
            total_tasks = 0
            done_tasks = 0
            # Initialize a list to store the titles of completed tasks
            done_titles = []
            # Loop through the todos data
            for todo in todos_data:
                # Increment the total number of tasks by 1
                total_tasks += 1
                # Check if the task is completed
                if todo.get("completed"):
                    # Increment the number of done tasks by 1
                    done_tasks += 1
                    # Append the task title to the list of done titles
                    done_titles.append(todo.get("title"))
            # Print the first line of output with
            # the employee name and the task progress
            print("Employee {} is done with tasks({}/{})"
                  .format(employee_name, done_tasks, total_tasks))
            # Loop through the list of done titles
            for title in done_titles:
                # Print each title with a tabulation and a space before it
                print("\t {}".format(title))
