from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import * 
import pytest 


def test_deque_from_cats():
        cat_1=Cat('cat_1')
        cat_2=Cat('cat_2')
        dog_1=Cat('dog_1')
        dog_2=Cat('dog_2')
        anima = AnimalShelter()
        anima.enqueue(cat_1)
        anima.enqueue(cat_2)
        anima.dequeue(cat_2)
        assert anima.dequeue('cat')==cat_2

def test_deque_from_dogs():
        cat_1=Cat('cat_1')
        cat_2=Cat('cat_2')
        dog_1=Dog('dog_1')
        dog_2=Dog('dog_2')
        anima = AnimalShelter()
        anima.enqueue(dog_1)
        anima.enqueue(dog_2)
        anima.dequeue(dog_2)
        assert anima.dequeue('dog')==dog_2


def test_dequeue_none():
        anima = AnimalShelter()

        assert anima.dequeue('m')==None

def test_deque_from_cat_from_cats_and_dogs():
        cat_1=Cat('cat_1')
        dog_1=Dog('dog_1')
        cat_2=Cat('cat_2')
        dog_2=Dog('dog_2')
        anima = AnimalShelter()
        anima.enqueue(cat_1)
        anima.enqueue(cat_2)
        anima.enqueue(dog_2)
        anima.enqueue(dog_2)
        anima.dequeue(cat_2)
        assert anima.dequeue('cat')==cat_2



def test_deque_from_dog_from_cats_and_dogs():
        cat_1=Cat('cat_1')
        dog_1=Dog('dog_1')
        cat_2=Cat('cat_2')
        dog_2=Dog('dog_2')
        anima = AnimalShelter()
        anima.enqueue(cat_1)
        anima.enqueue(cat_2)
        anima.enqueue(dog_2)
        anima.enqueue(dog_2)
        anima.dequeue(dog_2)
        assert anima.dequeue('dog')==dog_2
