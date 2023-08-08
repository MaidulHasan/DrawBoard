# ----------------------------------------
### The Queue Data Structure
# ----------------------------------------


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if len(self.queue) > 0 else None

    def read(self):
        return self.queue[0] if len(self.queue) > 0 else None
