from pprint import pprint
from queue import LifoQueue


class Stack:
    """Класс Стек"""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Вставка элемента"""
        self.items.append(item)

    def pop(self):
        """Удаление и возврат элемента"""
        return self.items.pop()

    def size(self):
        """Размер стека"""
        return len(self.items)

    def __str__(self):
        return f'{self.items}'


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)
print(stack.size())

print('Lifo Queue')
st = LifoQueue()
st.put(1)
st.put(2)
st.put(3)
pprint(st.queue)
print(st.get())
print(st.qsize())
