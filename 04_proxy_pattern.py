class Subject:
    def request(self):
        print("Subject: handling request")

class Proxy:
    def __init__(self, subject):
        self.subject = subject

    def _check_access(self) -> bool:
        print("Proxy: checking access before firing a real request")
        return True
    
    def _log_access(self):
        print("Proxy: logging the request time")

    def request(self):
        if self._check_access():
            self.subject.request()
            self._log_access()

if __name__ == "__main__":
    print("Client: Executing the client code with a real subject")
    subject = Subject()
    subject.request()

    print(50 * "-")
    print("Client: Executing the client code with a proxy")
    proxy = Proxy(subject)
    proxy.request()