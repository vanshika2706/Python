class Countdown:
    def init (self, n):
        self.n = n
    def iter (self) :
      while self.n > 0:
        yield self.n
        self.n -= 1
      for number in Countdown(5):
          print(number)
print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")