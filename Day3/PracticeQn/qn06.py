'''6. **Remove, Pop, and Del**  
   Given: tasks = ["email", "meeting", "lunch", "code", "review", "deploy"]  
   a) Remove "lunch" using remove()  
   b) Use pop(0) to remove and print the first task  
   c) Use del to delete the last two tasks  
   Print the list after each step.'''

tasks = ["email", "meeting", "lunch", "code", "review", "deploy"]
tasks.remove("lunch")
print(tasks)

print_firstTsk_remove=tasks.pop(0)
print(print_firstTsk_remove)
print(tasks)

del tasks[-2:]
print(tasks)



