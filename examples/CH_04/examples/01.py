class Person:
    """Defines a person by name"""

    from typing import Optional

    def __init__(self, fname: str, mname: Optional[str] = None, lname: Optional[str] = None):
        self.fname = fname
        self.mname = mname
        self.lname = lname

    def full_name(self) -> str:
        """This method returns the person's full name"""
        full_name = self.fname
        if self.mname is not None:
            full_name = f"{full_name} {self.mname}"
        if self.lname is not None:
            full_name = f"{full_name} {self.lname}"
        return full_name


def main():
    # Create some people
    people = [
        Person("John", "George", "Smith"),
        Person("Bill", lname="Thompson"),
        Person("Sam", mname="Watson"),
        Person("Tom"),
    ]

    # Print out the full names of the people
    x = 0
    for person in people:
        x += 1
        print(x, person.full_name())


if __name__ == "__main__":
    main()
