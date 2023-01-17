from collections import deque


class Dek(list):
    def push_front(self, item):
        self.insert(0, item)

    def pop_front(self):
        return self.pop(0)

    @property
    def size(self):
        return len(self)

d = Dek()
d.append(1)
d.append(2)
print(d)
d.push_front(3)
print(d)
d.pop()
d.pop_front()
print(d)
print(d.size)

print(f'{"DEk":<^20}')
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
d.popleft()
print(d)
print(len(d))
