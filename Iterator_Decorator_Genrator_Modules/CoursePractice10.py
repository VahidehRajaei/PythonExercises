class Counter:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        current=self.start
        if current>self.end:
            raise StopIteration
        self.start+=3
        return current

#-----------------------Sample-------------------------
counter1=Counter(10,100)
print('\nOutput\n',20*'_')
for i in counter1:
    print(i)
