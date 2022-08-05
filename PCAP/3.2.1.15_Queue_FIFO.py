class QueueError(IndexError):  # Choose base class for the new exception.
    pass

class Queue:
    def __init__(self):
        self.ql = []

    def res(self):
        return self.ql

    def put(self, elem):
        self.ql.append(elem)

    def get(self):
        if len(self.ql):
            elem = self.ql[0]
            del self.ql[0]
            return elem
        else:
            raise QueueError

que = Queue()
que.put(1)
que.put("dog")
que.put(False)

print('Queue is loaded', que.res(), '\n')

try:
    for i in range(4):
        print(f'Taking: {que.get()}, \tRemains: {que.res()}')
except:
    print('\n💥💥💥 Queue Error 💥💥💥')



# Functional approach counterpart (less code for the same example)
# -----------------------------------------------------------------

q = []

q.append(1)
q.append("dog")
q.append(False)

print('Queue is loaded', q, '\n')

try:
    for i in range(4):
        item = q[0]
        q = q[1:]
        print(f'Taking: {item}, \tRemains: {q}')
except:
    print('\n💥💥💥 Queue Error 💥💥💥')
