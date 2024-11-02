class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

import unittest
import logging


logging.basicConfig(level=logging.INFO, filename='runner_test.log', filemode='w', encoding='UTF-8',
                    format='%(levelname)s - %(message)s')

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('TestRunner', -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(20, 3)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner")


    def test_tournament(self):
        first = Runner('Вося', 10)
        second = Runner('Илья', 5)
        third = Runner('Арсен', 10)
        t = Tournament(101, first, second, third)

        try:
            res = t.start()
            self.assertEqual(len(res), 3)
            logging.info('"test_tournament" выполнен успешно')
        except Exception as err:
            logging.warning("Ошибка во время тестирования Tournament: %s", err)




if __name__ == "__main__":
    unittest.main()

