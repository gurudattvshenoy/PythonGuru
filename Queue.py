class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def remove(self):
        return self.items.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.remove())

