from queue import Queue


class Queues:
    def __init__(self):
        self.arr = []

    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop(0)

    def size(self):
        return len(self.arr)


q = Queues()
q.push(1)
q.push(2)
q.push(3)
print(q.arr)
print(q.pop())
print(q.size())

print(f'{"FIFO":>^20}')
q = Queue()
q.put(1)
q.put(2)
q.put(3)
print(q.queue)
print(q.get())
print(q.qsize())