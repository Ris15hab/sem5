class Employee:
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id
    
        
class Admin(Employee):
    def __init__(self,name,emp_id):
        super().__init__(name,emp_id)
        self.developers = []
        self.testers = []
    
    def registerDeveloper(self,developer):
        self.developers.append(developer)
    
    def getDevelopers(self):
        for i in self.developers:
            i.developer_details()
    
    def registerTester(self,tester):
        self.testers.append(tester)

    def getTester(self):
        for i in self.testers:
            i.tester_details()
            
    def getObject(self,emp_id,flg):
        if flg:
            for i in self.developers:
                if i.emp_id==emp_id:
                    return i
        else:
            for i in self.testers:
                if i.emp_id==emp_id:
                    return i

class Developer(Employee):
    def __init__(self,name,emp_id,language):
        super().__init__(name,emp_id)
        self.language = language
    
    def developer_details(self):
        print(f"Name: {self.name}\nEmp ID: {self.emp_id}\nLanguage: {self.language}")

class Tester(Employee):
    def __init__(self,name,emp_id,typ):
        super().__init__(name,emp_id)
        self.typ = typ
    
    def tester_details(self):
        print(f"Name: {self.name}\nEmp ID: {self.emp_id}\nType: {self.typ}")

class Manager(Employee):
    def __init__(self,name,emp_id):
        super().__init__(name,emp_id)
        self.employees = []
        self.temp = {}
    
    def addEmployee(self,employee,flg):
        self.employees.append(employee)
        self.temp[employee.emp_id] = flg

    def displayEmployees(self):
        for i in self.employees:
            if self.temp[i.emp_id] == 1:
                i.developer_details()
            else:
                i.tester_details()
    
    def removeEmployee(self,emp_id):
        for i in self.employees:
            if i.emp_id == emp_id:
                self.employees.remove(i)
                self.temp.pop(i.emp_id)
                break

    
admin = Admin('Admin','0')
manager = Manager('Manager','1')

while True:
    choice = int(input("Enter\n1.Add Developer\n2.Add tester\n3.Show Developers\n4.Show Testers\n5.Manager Dropdown\n0.exit:\n"))
    
    if choice == 1:
        name = input("Enter the name of the developer:\n")
        emp_id = input("Enter the employee id of the developer:\n")
        language = input("Enter the programming language of the developer:\n")
        developer = Developer(name,emp_id,language)
        admin.registerDeveloper(developer)

    elif choice == 2:
        name = input("Enter the name of the tester:\n")
        emp_id = input("Enter the employee id of the tester:\n")
        typ = input("Enter the testing type of the tester:\n")
        tester = Tester(name,emp_id,typ)
        admin.registerTester(tester)
    
    elif choice == 3:
        admin.getDevelopers()
    
    elif choice == 4:
        admin.getTester()
    
    elif choice == 5:
        choice1 = int(input("Enter\n1.Add developer under manager\n2.Add tester under manager\n3.remove employee under manager\n4.display employees under manager:\n"))
        if choice1 == 1:
            emp_id = input("Enter the employee id:\n")
            temp = admin.getObject(emp_id,1)
            manager.addEmployee(temp,1)

        if choice1 == 2:
            emp_id = input("Enter the employee id:\n")
            temp = admin.getObject(emp_id,0)
            manager.addEmployee(temp,0)
        
        if choice1 == 3:
            emp_id = input("Enter the employee id:\n")
            manager.removeEmployee(emp_id)
        
        if choice1 == 4:
            manager.displayEmployees()

    elif choice == 0:
        break