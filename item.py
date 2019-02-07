import datetime

class Item(object):

    def __init__(self, task, timestamp):
      self.timestamp = datetime.datetime.now
      self.task_comp = False
      self.task = task

define
task
complete
timestamp
