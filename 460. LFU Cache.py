# Leetcode - 460. LFU Cache (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 460. LFU Cache (Python language) -", "yellow"), colored("Hard", "red"))

class LFUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1

        elif len(self.cache) < self.capacity:
            self.cache[key] = [value, 1]

        else:
            least_used = min(
                self.cache,
                key=lambda k: self.cache[k][1]
            )

            del self.cache[least_used]
            self.cache[key] = [value, 1]

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache[key][1] += 1
        return self.cache[key][0]

lfu = LFUCache(2)
print(
    colored("Test 1:", "green"),
    lfu.put(1, 1),
    lfu.put(2, 2),
    lfu.get(1),
    lfu.put(3, 3),
    lfu.get(2),
    lfu.get(3),
    lfu.put(4, 4),
    lfu.get(1),
    lfu.get(3),
    lfu.get(4),
    "|",
    colored("Passed","green")
)