class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end and self.start % 2 == 0:
            start = self.start
            self.start += 2
            return start
        else:
            if self.start < self.end and self.start % 2 != 0:
                start = self.start + 1
                self.start += 2
                return start

        raise StopIteration


en = EvenNumbers(10, 25)
for i in en:
    print(i)

#ВТОРОЙ ВАРИАНТ РЕШЕНИЯ

class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            for val in range(self.start, self.end + 1):
                if val % 2 == 0:
                    print(val)
            raise StopIteration


en = EvenNumbers(11, 27)
for i in en:
    print(i) 
