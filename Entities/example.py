from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Address:
    street: str
    city: str

@dataclass_json
@dataclass
class Person:
    name: str
    age: int
    addresses: List[Address]  # List of Address objects

# Example JSON string
json_string = '''
{
    "name": "John",
    "age": 30,
    "addresses": [
        {
            "street": "123 Main St",
            "city": "New York"
        },
        {
            "street": "456 Elm St",
            "city": "Los Angeles"
        }
    ]
}
'''

# Parse JSON into Person object
person = Person.from_json(json_string)

print(person)
# Output: Person(name='John', age=30, addresses=[Address(street='123 Main St', city='New York'), Address(street='456 Elm St', city='Los Angeles')])
