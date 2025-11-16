#Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

#Process the task based on priority.
match priority:
  case "high":
    reminder = f"Reminder: '{task}' is a high priority task"

  case "medium":
   reminder = f"Reminder: '{task}' is a medium priority task"

  case "low":
   reminder = f"Reminder: '{task}' is a low priority task"

  case _:
    reminder = f"Reminder: '{task}' is an Unknown priority task"

#if statement to modify reminder if task is time bound
if time_bound == 'yes':
    reminder += f" that requires immediate attention today!"
    
else:
   reminder += f". Consider completing it when you have free time."

#Print output
print(reminder)
 
