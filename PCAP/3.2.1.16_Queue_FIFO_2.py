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

class SuperQueue(Queue):
    def isempty(self):
        return len(self.ql) == 0

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

print('Queue is loaded', que.res(), '\n')

for i in range(4):
    if not que.isempty():
        print(f'Taking: {que.get()}, \tRemains: {que.res()}')
    else:
        print('\n💡 EMPTY Queue')
