import asyncio
import time
from typing import List


class Runner:
    def __init__(self, name: str, age: int, speed=5):
        self.name = name
        self.age = age
        self.speed = speed


    async def running_marathon(self, distance: int):
        print("=" * 40)
        print(f"Начало пробежки {self.name} {time.strftime('%X')}")
        if self.age < 10:
            speed_factor = 0.7
            self.average_speed = self.speed * speed_factor
            print(f"Возраст {self.age} |  Скорость {self.average_speed} км/ч")
        elif 10 <= self.age < 20:
            speed_factor = 2
            self.average_speed = self.speed * speed_factor
            print(f"Возраст {self.age} | Скорость {self.average_speed} км/ч")
        elif 40 > self.age >= 20:
            speed_factor = 2.5
            self.average_speed = self.speed * speed_factor
            print(f"Возраст {self.age} | Скорость {self.average_speed} км/ч")
        elif self.age >= 40:
            speed_factor = 1.2
            self.average_speed = self.speed * speed_factor
            print(f"Возраст {self.age} | Скорость {self.average_speed} км/ч")
        else:
            print('Bye')
        self.time_to_run = (distance / self.average_speed) * 10
        await asyncio.sleep(self.time_to_run)
        print("=" * 45)
        print(f"Бегун {self.name} закончил пробежку в {time.strftime('%X')}")
        return self.time_to_run


    def __str__(self):
        return f"%10s | %12s | %12s | %.1f" % (self.name, self.age, self.average_speed, self.time_to_run)


async def main():
    runners = [Runner("Человек 1", 10), Runner("Человек 2", 30), Runner("Человек 3", 44), Runner("Человек 4", 12)]
    results: List = []
    runner_tasks = [asyncio.create_task(man.running_marathon(4)) for man in runners]
    results = await asyncio.gather(*runner_tasks)
    print("=" * 45)
    print(f"%10s | %12s | %12s | %12s" % ("Имя", "Возраст", "Скорость", "Затраченное время"))
    for run in runners:
        print(run)
    print("end")
    total_result = max(results)-min(results)
    print(f"Самый быстрый бегун , быстрее медленного на '%.1f' минуты" % (total_result))


asyncio.run(main())

