class Manager(object):
  # Creating a function that takes an argument.
    def PrintList(self):
        # This will open my .txt file with read permissions.
        target = open("todos.txt", 'r')
        # This will print your .txt file.
        print(target.read())
        # This will close the target and remove the space used to open it.
        target.close()
  # Creating a function that takes arguments.
    def AddItems(self):
        # This will add items and append it to my .txt file.
        target = open("todos.txt", 'a')
        # This allows me to add an input to my list. It also says add a task to prompt you to type.
        add = target.write(input("""Add a Task
>""")+ "\n")
        # This will just add information to the end of the file.
        target.close()
  # Creating a function that takes arguments.

#I wanted to be able to choose what to do when you first run the file.
# def start():
    # print("1. View todo list")
    # print("2. Add to the todo list")
    # print("3. Change todo state")
    # print("4. Quit")

    #  beginning = input('-> ')


add = Manager()
add.AddItems()


#text = Manager()
#text.PrintList()
