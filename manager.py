class manager(object):
  # Creating a function that takes an argument.
    def PrintList(self):
        # This will open my .txt file with read permissions.
        target = open(todo.txt, 'r')
        # This will print your .txt file.
        print(target.read())
        # This will close the target and remove the space used to open it.
        target.close()
  # Creating a function that takes arguments.
    def AddItems(self, item):
        # This will add items and append it to my .txt file.
        target = open(todo.txt, 'a+')
        # This will just add information to the end of the file.
        target.append()
  # Creating a function that takes arguments.
    def CompleteItem(self, item):
