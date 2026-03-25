class Gender:
  MALE = "male"
  FEMALE = "female"


class Person:

  def __init__(self, firstName, lastName, gender):
    self.firstName = firstName
    self.lastName = lastName
    self.gender = gender


class Employee(Person):

  def __init__(self, firstName, lastName, gender, employeeId):
    super().__init__(firstName, lastName, gender)
    self.employeeId = employeeId
    self.department = None

  def department(self):
    return self.department

  def setDepartment(self, department):
    self.department = department


class DepartmentManager(Employee):
  pass


class Department:

  def __init__(self, name):
    self.name = name
    self.employeesById = {}
    self.manager = None

  def addEmployee(self, employee):
    self.employeesById[employee.employeeId] = employee
    employee.setDepartment(self)

  def setManager(self, manager):
    self.addEmployee(manager)
    self.manager = manager

  def employeeCount(self):
    return len(self.employeesById)

  def managerCount(self):
    return 1 if self.manager is not None else 0

  def countGenders(self):
    females = 0
    males = 0

    for empId in self.employeesById:
      employee = self.employeesById[empId]
      if employee.gender == Gender.FEMALE:
        females += 1
      else:
        males += 1

    return females, males


class Company:

  def __init__(self, name):
    self.name = name
    self.departmentsByName = {}

  def addDepartment(self, department):
    self.departmentsByName[department.name] = department

  def departmentCount(self):
    return len(self.departmentsByName)

  def employeeCount(self):
    total = 0
    for depName in self.departmentsByName:
      total += self.departmentsByName[depName].employeeCount()
    return total

  def managerCount(self):
    total = 0
    for depName in self.departmentsByName:
      total += self.departmentsByName[depName].managerCount()
    return total

  def departmentWithMostEmployees(self):
    if self.departmentCount() == 0:
      return None

    bestDepartment = None
    bestCount = -1

    for depName in self.departmentsByName:
      department = self.departmentsByName[depName]
      count = department.employeeCount()
      if count > bestCount:
        bestCount = count
        bestDepartment = department

    return bestDepartment

  def genderPercentage(self):
    totalEmployees = self.employeeCount()
    if totalEmployees == 0:
      return 0.0, 0.0

    females = 0
    males = 0

    for depName in self.departmentsByName:
      f, m = self.departmentsByName[depName].countGenders()
      females += f
      males += m

    femalePercent = (females * 100.0) / totalEmployees
    malePercent = (males * 100.0) / totalEmployees
    return femalePercent, malePercent


def main():
  company = Company("BugglaFirma")

  it = Department("IT")
  rk = Department("RK")

  company.addDepartment(it)
  company.addDepartment(rk)

  e1 = Employee("Enes", "Duschäoor", Gender.FEMALE, "E1")
  e2 = Employee("Meister", "Eder", Gender.MALE, "E2")
  m1 = DepartmentManager("Stefan", "Keks", Gender.FEMALE, "M1")

  it.addEmployee(e1)
  it.addEmployee(e2)
  it.setManager(m1)

  print("Abteilungen:", company.departmentCount())
  print("Mitarbetier:", company.employeeCount())
  print("Abteilungsleiter:", company.managerCount())

  biggest = company.departmentWithMostEmployees()
  if biggest is not None:
    print("Größte Abteilung:", biggest.name)

  femalePercent, malePercent = company.genderPercentage()
  print(f"Frauen %:", round(femalePercent, 1), "Männer %:", round(malePercent, 1))


if __name__ == "__main__":
  main()
