#CRUD CREATE READ UPDATE DELETE
task_list = []

 while True:

  user_option = input("""
  1. Add task
  2. View task
  3. Mark task as completed
  4. Remove task
  5. End Program

  """)

  if user_option == "1":
    user_task = input("Enter a task: ")

    task_list.append(
        {
            "task": user_task,
            "completed": False
        }
    )


    print("Task added")
  elif user_option == "2"
    for i, task in enumerate(task_list):
      print(i+1, task["task"], "----------", task["completed"])
  elif user_option == "3"
    user_task_index = int(input("Enter a task index: "))
    task_list[user_task_index-1]["completed"] = True
    print("Task marked as completed")

  elif user_option == "4":
      user_task_index = int(input("Enter a task index: "))
      task_list.pop(user_task_index-1)
      print("Task removed")
  elif user_option == "5":
      print("Program ended")
      break
  else:
      print("Invalid option")
