class DataStream:

    def __init__(self, value: int, k: int):
        self.qw = deque()
        self.val = value
        self.k = k
        self.cnt = 0
        self.rt = 0

    def consec(self, num: int) -> bool:
        self.qw.append(num)
        self.cnt += 1
        if self.qw[self.cnt-1] == self.val:
            self.rt += 1
        else:
            self.rt = 0

        if self.k == self.cnt:
            self.qw.popleft()
            self.cnt -= 1
            if self.rt >= self.k:
                return True
        return False
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
