class RecentCounter:

    def __init__(self):
        self.q = []
        self.length = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        self.length+=1
        counter = 0
        for i in self.q:
            if i >= t-3000 and i <= t:
                counter+=1
        return counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)