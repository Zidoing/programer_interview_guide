#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-28.


class Pet:

    def __init__(self, type):
        self.type = type

    def get_pet_type(self):
        return self.type


class Dog(Pet):

    def __init__(self):
        super(Dog, self).__init__("dog")


class Cat(Pet):

    def __init__(self):
        super(Cat, self).__init__("cat")


from queue import Queue


class DogQueue:

    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def get_type(self):
        return self.pet.get_pet_type()


class CatQueue:

    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def get_type(self):
        return self.pet.get_pet_type()


class DogCatQueue:

    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
        self.count = 0

    def add_pet(self, pet):
        if pet.get_pet_type() == "dog":
            self.dog.put(DogQueue(pet, self.count))
        elif pet.get_pet_type() == "cat":
            self.cat.put(CatQueue(pet, self.count))
        else:
            raise TypeError

        self.count += 1
