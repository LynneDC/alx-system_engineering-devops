#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        sys.exit(1)

    employee_name = response.json().get("name")
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}): "
          .format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print(f"\t{task.get('title')}")
