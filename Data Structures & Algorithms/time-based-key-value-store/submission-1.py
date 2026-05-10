class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = {}
        self.dic[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic:
            if timestamp in self.dic[key]:
                return self.dic[key][timestamp]
            while timestamp >= 0:
                timestamp -= 1
                if timestamp in self.dic[key]:
                    return self.dic[key][timestamp]
        return ""
        