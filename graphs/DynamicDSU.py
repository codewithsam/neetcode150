class DynamicDSU:
    def __init__(self, n=0):
        self.parent = []
        self.size = []
        self.map = {}  # element -> index

    def make_set(self, elem):
        if elem not in self.map:
            idx = len(self.parent)
            self.map[elem] = idx
            self.parent.append(idx)
            self.size.append(1)
        return self.map[elem]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                # root_v is bigger, attach u → v
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                # root_u is bigger, attach v → u
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]

    def find(self, u):
        idx = self.make_set(u)
        if self.parent[idx] != idx:
            self.parent[idx] = self.find_by_index(self.parent[idx])
        return self.parent[idx]

    def find_by_index(self, idx):
        """Helper to find root by internal index with path compression."""
        if self.parent[idx] != idx:
            self.parent[idx] = self.find_by_index(self.parent[idx])
        return self.parent[idx]

    def connected(self, u, v):
        return self.find(u) == self.find(v)


dsu = DSU()

dsu.make_set("A")
dsu.make_set("B")
dsu.make_set("C")
dsu.make_set("D")

dsu.union("A", "B")
dsu.union("B", "C")


print(dsu.connected("A", "C"))  # True
print(dsu.connected("A", "D"))  # False

print(dsu.find("A"))  # root of A, B, C
print(dsu.find("B"))  # same root as A
print(dsu.find("C"))  # same root as A
print(dsu.find("D"))  # its own root
