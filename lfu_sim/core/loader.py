class DataLoader:
    def get(self):
        raise NotImplementedError()


class FileDataLoader(DataLoader):
    def __init__(self, source):
        self.source_directory = source

    def get(self):
        with open(self.source_directory) as file:
            for line in file.readlines():
                block = line.split()[0]
                yield block


if __name__ == "__main__":
    f = FileDataLoader("linkbench.trc")
    for index, value in enumerate(f.get()):
        if index >= 10: break
        print(index, value)
