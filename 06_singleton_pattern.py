class RoundRobin:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if not hasattr(self, "servers"):
            self.servers = []
            self.index = 0

    def add_server(self, server):
        self.servers.append(server)

    def get_next_server(self):
        if not self.servers:
            raise ValueError("No servers available")
        
        self.index = (self.index + 1) % len(self.servers)
        return self.servers[self.index]
    
if __name__ == "__main__":
    rr = RoundRobin()
    rr.add_server("Server 1")
    rr.add_server("Server 2")
    rr.add_server("Server 3")
    rr.add_server("Server 4")
    rr.add_server("Server 5")

    rr2 = RoundRobin()
    print(rr is rr2)
    
    for _ in range(10):
        print(rr.get_next_server())