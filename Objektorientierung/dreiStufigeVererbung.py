class Grandparent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"I am the grandparent. Name: {self.name}"

    def get_age(self):
        return self.age


class Parent(Grandparent):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def describe(self):
        return f"I am the parent. Name: {self.name}"


class Child(Parent):
    def __init__(self, name, age, job, school):
        super().__init__(name, age, job)
        self.school = school

    def describe(self):
        return f"I am the child. Name: {self.name}"

def main():
    g = Grandparent("Sepp", 70)
    p = Parent("Robert", 45, "Engineer")
    c = Child("Larry", 15, "Engineer", "HTL")

    print(g.describe(), ", Age:", g.get_age())
    print(p.describe(), ", Age:", p.get_age())
    print(c.describe(), ", Age:", c.get_age())


if __name__ == "__main__":
    main()
