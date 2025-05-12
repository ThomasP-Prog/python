"""
Create a base class Employee with __init__(self, name: str, employee_id: str, salary: float).
Add a method get_details(self) that returns a string with the employee's name, ID, and salary.
Create a subclass Manager that inherits from Employee. Its __init__ should take name, employee_id, salary, and an additional department: str. 
It should call the parent's __init__ and also store the department.
Override get_details(self) in Manager to include the department information. 
It should first call the parent's get_details() using super() and then append the department info to that result.

Sample Data: Create an Employee and a Manager instance and print their details.
"""

# --- Superclass ---
class Employee:
    def __init__(self, name:str, employee_id:str, salary:float) -> None:
        """Initialize employee"""
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_details(self) -> str:
        """Returns a str with employee details"""
        return f"Employee name : {self.name}, id : {self.employee_id}, salary : {self.salary}"
    
# --- Subclass ---
class Manager(Employee):
    def __init__(self, name:str, employee_id:str, salary:float, department:str):
        """Initialize Manager"""
        super().__init__(name, employee_id, salary)
        self.department = department

    def get_details(self) -> str:
        """Override Employee get_details()"""
        employee_details_str = super().get_details()
        return f"{employee_details_str}, department : {self.department}"
    
def main() -> None:
    """main function"""
    employee1 = Employee("bob","id_01",1234.5)
    manager1 = Manager("D'Jack","id_00",2345.6,"pet")

    employee1_info = employee1.get_details()
    manager1_info = manager1.get_details()
    print(employee1_info)
    print(manager1_info)

if __name__ == "__main__":
    main()