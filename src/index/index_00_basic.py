from dataclasses import dataclass
from typing import List, TypedDict

from typingjson import (
    as_typed_dict,
    asdataclass,
    dataclass_asjson,
    typed_dict_asjson,
    typingjson,
)


# dataclass


@dataclass
class Music:
    name: str


# if 'Person' is not a dataclass the
# 'typingjson' decorator will call the
# 'dataclass' decorator
@typingjson
class Person:
    name: str
    age: int
    musics: List[Music]


jsondict = dict(name=b'John', age='40', musics=[dict(name='Imagine')])
person = asdataclass(jsondict, Person)

print('dataclass:')
print(person)
print(dataclass_asjson(person))
print()


# TypedDict


@typingjson
class Music(TypedDict):
    name: str


# This decorator is required because
# we need to track the annotations
@typingjson
class Person(TypedDict):
    name: str
    age: int
    musics: List[Music]


jsondict = dict(name=b'John', age='40', musics=[dict(name='Imagine')])
person = as_typed_dict(jsondict, Person)

print('TypedDict:')
print(person)
print(typed_dict_asjson(person, Person))
