class Allocator:
    def __init__(self):
        self.chunk_size = 4096
        
    def print_stats(self):
        print("Arena: XX MB")
        print("In-use: XX MB")
        print("Utilization: 0.XX")


    def malloc(self, id, size):
        pass
    
    def free(self, id):
        pass


if __name__ == "__main__":
    allocator = Allocator()
    
    with open ("./input.txt", "r") as file:
        n=0
        for line in file:
            req = line.split()
            if req[0] == 'a':
                allocator.malloc(int(req[1]), int(req[2]))
            elif req[0] == 'f':
                allocator.free(int(req[1]))

            # if n%100 == 0:
            #     print(n, "...")
            
            n+=1
    
    allocator.print_stats()