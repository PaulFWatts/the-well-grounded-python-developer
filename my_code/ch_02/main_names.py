from utilities import names
from utilities import informal
from utilities import casual
from utilities import account

community = [{"title": "Mr.", "fname": "John", "lname": "Smith"} for x in range(3)]

for person in community:
    tone = account.get_tone(person)
    if tone == "formal":
        get_name = names.get_name
    elif tone == "informal":
        get_name = informal.get_name
    elif tone == "casual":
        get_name = casual.get_name
    else:
        get_name = names.get_name

    # other code that calls get_name many times
    print(get_name(person))
