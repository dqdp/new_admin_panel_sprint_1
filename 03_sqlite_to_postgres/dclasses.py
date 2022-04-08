import uuid

from dataclasses import dataclass, field
from datetime import date, datetime


@dataclass
class Filmwork:
    id: uuid.UUID
    title: str
    description: str
    creation_date: date
    file_path: str
    rating: float
    type: str
    created: datetime
    updated: datetime
    
    
@dataclass
class Genre:
    id: uuid.UUID
    name: str
    description: str
    created: str
    updated: str


@dataclass
class GenreFilmwork:
    id: uuid.UUID
    filmwork_id: uuid.UUID
    genre_id: uuid.UUID
    created: str
    
    
@dataclass
class Person:
    id: uuid.UUID
    full_name: str
    created: str
    updated: str
    

@dataclass
class PersonFilmwork:
    id: uuid.UUID
    filmwork_id: uuid.UUID
    person_id: uuid.UUID
    role: str
    created: str
    