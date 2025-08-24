class RecentCounter:

    def __init__(self):
        self.q = []
        self.counter = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        self.counter += 1
        while self.q[0] < t - 3000:
            self.q.pop(0)
            self.counter -= 1
        return self.counter

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)