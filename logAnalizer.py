"""
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
        super().__init__()
        self.language = self.language + ["German"]

    def __str__(self):
        return f"languages {self.language}"




list = []

a = LogEntery("1.1.1", "online", "28/8/2026")
b = LogEntery("1.1.2", "ofline", "21/8/2026")

list.append(a)
list.append(b)


for object in list:
    print(object)
"""



"""
class Dog:

    specie = "Canis familiaris"


    def __init__(self, name, age, breed):
        self.name = name 
        self.age = age
        self.breed  = breed



    def __str__(self):
        return f"{self.name} {self.age} {self.breed}"


    def speak(self, sound):
        return f"{self.name} Bark {sound}"


class Bulldog(Dog):


    def speak(self, sound="wof"):
        return super().speak(sound)

class Dachshund(Dog):

    def speak(self, sound="rof"):
        return super().speak(sound)

    
class RussellTerrier(Dog):

   def speak(self, sound="miau"):
       return super().speak(sound)

"""


class User:



    passwords = [{"name": "Admin", "pass": "123"}]


    def __init__(self, name, age, ip_adress):
        self.name = name
        self.age = age
        self.ip_adress = ip_adress


    def __str__(self):
        return f"\n-Name: {self.name};\n-Age: {self.age};\n-IP: {self.ip_adress}"


    def create_password(self, password):
        self.passwords.append({"name": self.name, "pass": password})
        return self.passwords


    def log_in(self, password_given):
        if self.passwords[self.name] == password_given:
            return True
        else:
            return False

juan = User("juan", 42, "1.1.1.1")
print(juan)
juan.create_password("abc")

paulo = User("Paulo", 47, "2.2.2.2")
print(paulo)
print(paulo.create_password("my_pass"))


print(paulo.log_in("my_pass"))
print(paulo.log_in("123"))


