class CacheAlgorithm:
    def update(self, data):
        raise NotImplementedError()

class LFU(CacheAlgorithm):
    def update(self, data):
        ...