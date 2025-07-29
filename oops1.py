class Employee:
    def __init__(self):
        self.id=1
        self.salary=25000
        self.designation='Data Engineer'

    def travel(self,destination):
        print(f'Sam is travelling to {destination}')

ash = Employee()

#print(ash.salary)
ash.travel('Mumbai')