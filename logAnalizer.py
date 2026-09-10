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



    passwords = []

    adimin_pass = "Admin.Pass"

    def __init__(self, name, age, ip_adress):
        self.name = name
        self.age = age
        self.ip_adress = ip_adress


    def __str__(self):
        return f"\n-Name: {self.name};\n-Age: {self.age};\n-IP: {self.ip_adress}"


    def create_password(self, password):
        self.passwords.append({"name": self.name, "pass": password})
        return self.passwords

    def remove_user(self, username:str, pass_given: str):
        if pass_given == self.adimin_pass:

            for person in self.passwords:

                
                if username == person['name']:
                    self.passwords.remove(person)
                    return self.passwords
        else:
            return f"The password given is wrong."
    

    def log_in(self, password_given):
        #print(password_given)
        for user in self.passwords:
            if user["name"] == self.name:
                #print(user)
                #print(self.name)
                if user['pass'] == password_given and user['name'] == self.name:
                    return True
                else:
                    return False



    


"""
#alias 
func = admin.log_in
func_2 = func

print(func("123"))
print(func_2("admin"))
"""


user1 = User("john", 34, "1.1.1.1")
user2 = User("Dani", 42, "2.2.2.2")
user3 = User("Abel", 63, "3.3.3.3")
user4 = User("jamon", 32, "4.4.4.4")

user1.create_password("12345")
user2.create_password("abcde")
user3.create_password("sun_123")


print(user1.remove_user("Dani", user1.adimin_pass)) 
print(user2.log_in("abcde"))
print(user3.log_in("12345"))
print(user4.log_in(user4.adimin_pass))