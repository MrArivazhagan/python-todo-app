FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
     Read a text file and return the list of to-do items
    """
    with open(filepath, "r") as file:
        local_todos = file.readlines()
    return local_todos


def write_todos(todos_list, filepath=FILEPATH):
    """
    Write to-do item list in text file
    """
    with open(filepath, "w") as file:
        file.writelines(todos_list)


# print("running the file due to import")
if __name__ == "__main__":
    print("User wants to run this file")
