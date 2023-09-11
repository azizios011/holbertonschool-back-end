#!/usr/bin/python3


import json
import requests
import sys

def export_tasks_to_json(user_id):
    """
    Export tasks for a given user to a JSON file.

    Args:
        user_id (str): The user's ID for whom tasks will be exported.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch the user's data
    user_response = requests.get(f"{base_url}/users/{user_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch the user's tasks
    tasks_response = requests.get(f"{base_url}/todos?userId={user_id}")
    tasks_data = tasks_response.json()

    # Create a list to store task data
    task_list = []

    # Iterate through tasks and format them
    for task in tasks_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        task_list.append(task_dict)

    # Create a dictionary to store the formatted tasks
    result_dict = {user_id: task_list}

    # Export the data to a JSON file
    with open(f"{user_id}.json", "w") as json_file:
        json.dump(result_dict, json_file, indent=4)

    print(f"Data exported to {user_id}.json")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_tasks_to_json(user_id)
