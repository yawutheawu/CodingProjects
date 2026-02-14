class SequenceIterator:
    def __init__(self,sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

for i in SequenceIterator([10,20,30,40,50]):
    print(i)

print()

class SquareIterator:
    def __init__(self,sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index] ** 2
            self._index += 1
            return item
        else:
            raise StopIteration

for i in SquareIterator([10,20,30,40,50]):
    print(i)

print()

class FibonacciIterator:
    def __init__(self, start = 10, stop=None):
        if stop == None:
            self._index = 0
            self._stop = start
        else:
            self._index = start
            self._stop = stop
        tempVar = 0
        self._current = 0
        self._next = 1
        while tempVar < self._index:
            tempVar += 1
            self._current, self._next = (
                self._next,
                self._current + self._next
            )
        del tempVar

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < self._stop:
            self._index += 1
            fib_number = self._current
            self._current, self._next = (
                self._next,
                self._current + self._next
            )
            return fib_number
        else:
            raise StopIteration

startPoint = 0
endPoint = 10

for k,i in enumerate(FibonacciIterator(startPoint,endPoint+1)):
    print(startPoint + k,i)
