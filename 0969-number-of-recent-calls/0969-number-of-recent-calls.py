class RecentCounter:

    def __init__(self):
        self.requests=[]
        self.start=0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.start]<t-3000:
            self.start+=1
        return len(self.requests)-self.start

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)