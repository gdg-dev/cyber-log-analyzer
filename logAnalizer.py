
#class stuctur
class LogEntery:
    language = ["English"]
    def __init__(self, ip_adress, status, timestamp):
        self.ip_adress = ip_adress
        self.status = status
        self.timestamp = timestamp


    def __str__(self):
        return f"{self.language}, {self.ip_adress}, {self.status} {self.timestamp}"



class Information(LogEntery):


    def __init__(self):
        super().__init__(self.language)
        self.language = self.language + ["German"]

    def __str__(self):
        return f"languages {self.language}"




list = []

a = LogEntery("1.1.1", "online", "28/8/2026")
b = LogEntery("1.1.2", "ofline", "21/8/2026")
c = Information()
list.append(a)
list.append(b)
print(c)

for object in list:
    print(object)
