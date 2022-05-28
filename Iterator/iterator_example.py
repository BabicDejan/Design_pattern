from __future__ import annotations
from ast import Or
from collections.abc import Iterable, Iterator
from gc import collect
from multiprocessing import Value
from typing import Any, List

#to implement iterator in python, there are 2 abstract classes to bi imported, Iterable and Iterator

#to create an iterator pattern in python, we need an class which extends Iterator class, as well as class which is going to extend Iterable (that class is collection)

class OrderIterator(Iterator):

#we need position atribute and we need indicator if we are going in straight or reverse path in iterations

    _position : int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0
    
    def __next__(self):
        #method next must return the next item in sequence. On reaching the end it must raise StopIteration()
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class WordsCollection(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection
    
    def __iter__(self) -> OrderIterator:
        #ova metoda vraće iterator klasu, koja će sadržati elemente kolekcije

        return OrderIterator(self._collection)
    
    def get_reverse_iterator(self) -> OrderIterator:
        return OrderIterator(self._collection, True)
    
    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")
    collection.add_item("Fourth")
    collection.add_item("Fifth")

    print("Iterating from first element: ")
    #we use join because the iterator only returns locations in memory, as join access the values
    print("\n".join(collection))

    print("\n")
    print("\n".join(collection.get_reverse_iterator()))

    print("\n")
    print("Job finished :D")


