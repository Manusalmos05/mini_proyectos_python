from datetime import datetime

class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()
     
