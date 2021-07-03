class UF:
    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.size = [1] * n

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        while self.id[x] != x:
            self.id[x] = self.id[self.id[x]]
            x = self.id[x]
        return x

    def union(self, x, y):
        x_id = self.find(x)
        y_id = self.find(y)
        if x_id == y_id:
            return
        if self.size[x_id] < self.size[y_id]:
            self.id[x_id] = y_id
            self.size[y_id] += self.size[x_id]
        else:
            self.id[y_id] = x_id
            self.size[x_id] += self.size[y_id]

        self.count -= 1
