from django.db import models

# Create your models here.
class Contact:
    def __init__(self, name, surname, number) -> None:
        self.name = name
        self.surname = surname
        self.number = number

    def __str__(self) -> str:
        return f"""
        <h3>{self.name} {self.surname}</h3>
        <p>{self.number}</p>
        """
    
    
contacts = [
    Contact("Name1", "Surname1", "(001) 111-1111"),
    Contact("Name2", "Surname2", "(002) 222-2222"),
    Contact("Name3", "Surname3", "(003) 333-3333"),
    Contact("Name4", "Surname4", "(004) 444-4444"),
]