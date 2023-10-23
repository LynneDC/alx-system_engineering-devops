#!/usr/bin/python3
"""Python script that, using this REST API"""


import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    employees = response.json()

    todo_all_employees = {}
    for employee in employees:
        employee_id = employee.get("id")
        employee_name = employee.get("name")
        url = "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
        response = requests.get(url)
        todos = response.json()
        task_list = []
        for task in todos:
            task_dict = {"task": task.get("title"),
                         "completed": task.get("completed"),
                         "username": employee_name}
            task_list.append(task_dict)
        todo_all_employees[employee_id] = task_list

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(todo_all_employees, outfile)
