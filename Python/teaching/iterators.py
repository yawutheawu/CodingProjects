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
    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

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
        
for k,i in enumerate(FibonacciIterator(99999999)):
    print(i)
    print(k)
