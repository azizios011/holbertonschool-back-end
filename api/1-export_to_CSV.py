#!/usr/bin/python3

"""
This module exports task data to CSV format.

Author: Your Name
Date: September 13, 2023
"""


import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"

def user_info(id):

     """
    Retrieve user information and export tasks to CSV.

    Args:
        id (int): The user's ID.

    Returns:
        None
    """

    total_tasks = 0

    response = requests.get(todos_url).json()
    for task in response:
        if task['userId'] == id:
            total_tasks += 1

    num_lines = 0
    with open(str(id) + ".csv", 'r') as f:
        for line in f:
            if not line.strip():
                continue
            num_lines += 1

    if total_tasks == num_lines:
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")

if __name__ == "__main__":
    user_info(int(sys.argv[1]))
