FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):

    """ reads existing text file and returns to-do item stored in that file."""

    with open(filepath, 'r') as file_get:
        todos_local = file_get.readlines()
        return todos_local

def write_todos(todos_arg ,filepath=FILEPATH):
     with open(filepath, 'w') as file:
            file.writelines(todos_arg)



#in-case if you dont want to print content of this file or a program use the following method  
if __name__ == "__name__":
     print("hello")
     print(get_todos())