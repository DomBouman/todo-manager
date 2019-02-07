import datetime

class Item(object):
  # Basically creates an empty container that you can fill with timestamp and tasks.
    def __init__(self, task, timestamp):
      self.timestamp = datetime.datetime.now
      self.task_comp = False
      self.task = task
