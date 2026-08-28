
#class stuctur
class LogEntery:
    
    def __init__(self, ip_adress, status, timestamp):
        self.ip_adress = ip_adress
        self.status = status
        self.timestamp = timestamp


    def __str__(self):
        return f"{self.ip_adress}, {self.status} {self.timestamp}"


a = LogEntery("1.1.1", "online", "28/8/2026")
print(a)