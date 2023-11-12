class Person:
    #Инициализируем поля класса Person
    def __init__(self, firstName: str, secondName: str, thirdName: str, dictionary: dict) -> None:
        self.firstName = firstName
        self.secondName = secondName
        self.thirdName = thirdName
        self.dictionary = dictionary
    #Делаем функции, для получения данных из полей
    def GetName(self) -> str:
        return f"{self.secondName} {self.firstName} {self.thirdName}"
    
    def GetPhone(self, key = "private") -> int:
        return self.dictionary.get(key)
    
    def GetWorkPhone(self) -> int:
        return self.GetPhone("work")
    
    def GetSmsText(self) -> str:
        return f'Уважаемый {self.firstName} {self.thirdName}! \
            Примите участие в нашем беспроигрышном конкурсе для физических лиц'
    

class Company:
    #Инициализируем поля класса Company, передаём *arg, а именно объекты класса Person
    def __init__(self, companyName: str, companyType: str, dictionary: dict, *arg: Person) -> None:
        self.companyName = companyName
        self.companyType = companyType
        self.dictionary = dictionary
        self.person = arg
    #Создаём функцию, которая возвращает верное значение номера    
    def GetPhone(self, key = "contact") -> int:
        if key in self.dictionary:
            return self.dictionary.get(key)
        for person in self.person:
            number = person.GetWorkPhone()
            if number:
                return number
        
    def GetName(self) -> str:
        return self.companyName
    
    def GetSmsText(self) -> str:
        return f'Для компании {self.companyName} есть супер предложение! \
            Примите участие в нашем беспроигрышном конкурсе для {self.companyType}.'

#Создаём функцию SendSMS, которая принимает в себя *объекты, а именно классов Company / Person    
def sendSMS(*objects) -> str:
    for e in objects:
        if e.GetPhone():
            print(f"Отправлено СМС на номер {e.GetPhone()} c текстом: {e.GetSmsText()}")
        else:
            print(f'Не удалось отправить сообщение абоненту: {e.GetName()}')    

#Тесты
person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private":789})
person2 = Person("Ivan", "Petrovich", "Sidorov", {"work":789})
person3 = Person("John", "Unknown", "Doe", {})
company1 = Company("Cell", "AO", {"contact":111}, person1, person2)
company2 = Company("Bell", "OOO", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person3)
sendSMS(person1, person2, person3, company1, company2, company3)
