import uuid
from dataclasses import dataclass
from datetime import date, datetime


class TimestampMixin:
    def __post_init__(self):
        if type(self.created) == str:
            self.created = datetime.strptime(self.created + '00', "%Y-%m-%d %H:%M:%S.%f%z")
        if type(self.updated) == str:
            self.updated = datetime.strptime(self.updated + '00', "%Y-%m-%d %H:%M:%S.%f%z")


@dataclass
class Filmwork(TimestampMixin):
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
class Genre(TimestampMixin):
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

    def __post_init__(self):
        if type(self.created) == str:
            self.created = datetime.strptime(self.created + '00', "%Y-%m-%d %H:%M:%S.%f%z")


@dataclass
class Person(TimestampMixin):
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

    def __post_init__(self):
        if type(self.created) == str:
            self.created = datetime.strptime(self.created + '00', "%Y-%m-%d %H:%M:%S.%f%z")
