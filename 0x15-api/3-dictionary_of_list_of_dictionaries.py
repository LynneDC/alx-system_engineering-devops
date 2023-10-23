#!/usr/bin/env python3
"""
Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import json


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    employees = response.json()

    todo_all_employees = {}
    for employee in employees:
        employee_id = employee.get("id")
        employee_name = employee.get("name")
        url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        response = requests.get(url)
        todos = response.json()
        task_list = []
        for task in todos:
            task_dict = {"task": task.get("title"), "completed": task.get("completed"), "username": employee_name}
            task_list.append(task_dict)
        todo_all_employees[employee_id] = task_list

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(todo_all_employees, outfile)
