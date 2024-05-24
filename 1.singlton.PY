class count_users():
    count = 0
    def count_users(self):
        self.count += 1
        
    def result(self):
        return self.count

class singleton(count_users):
#lazy intialization
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def creat():
        return singleton()     

c1 = singleton.creat()
c1.count_users()
c2 = singleton.creat()
c2.count_users()
print(c2.result())  