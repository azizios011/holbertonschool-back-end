#!/usr/bin/python3
"""Script that uses a REST API to get information
about an employee's TODO list progress"""


import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]

    if not employee_id.isdigit():

        print("Usage: {} <employee ID>".format(sys.argv[0]))
        sys.exit(1)
    users_url =
    "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    users_response = requests.get(users_url)

    if users_response.status_code == 200:

        users_data = users_response.json()

        employee_name = users_data.get("name")

        todos_url = "https://jsonplaceholder.typicode.com/todos"

        todos_response = requests.get(todos_url,
                                      params={"userId": employee_id})

        if todos_response.status_code == 200:

            todos_data = todos_response.json()

            total_tasks = 0

            done_tasks = 0

            done_titles = []

            for todo in todos_data:

                total_tasks += 1

                if todo.get("completed"):

                    done_tasks += 1

                    done_titles.append(todo.get("title"))

            print("Employee {} is done with tasks({}/{})"
                  .format(employee_name, done_tasks, total_tasks))

            for title in done_titles:

                print("\t {}".format(title))
