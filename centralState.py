import redis


class CentralState:
    def __init__(self, port) -> None:
        self.r = redis.Redis(host="localhost", port=port, decode_responses=True)

    def addValue(self, key, value) -> bool:
        return self.r.set(key, value)

    def getValue(self, key) -> str:
        return self.r.get(key)
