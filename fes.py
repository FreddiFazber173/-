class Animal:
    def __init__(self, name, age, weight, kind, food):
        self.name = name          
        self.age = age            
        self.weight = weight      
        self.kind = kind          
        self.food = food          

    def make_sound(self):
        return self.name + " издает звук."

    def eat(self):
        return self.name + " ест еду: " + self.food + "."


class Reptile(Animal):
    def __init__(self, name, age, weight, kind, food, scale_type, is_poisonous):
        super().__init__(name, age, weight, kind, food)
        self.scale_type = scale_type      
        self.is_poisonous = is_poisonous    

    def crawl(self):
        return self.name + " медленно и опасно ползет."

    def shed_skin(self):
        return self.name + " меняет старую кожу."


class Amphibian(Animal):
    def __init__(self, name, age, weight, kind, food, skin_type, water_needed):
        super().__init__(name, age, weight, kind, food)
        self.skin_type = skin_type          
        self.water_needed = water_needed    

    def swim(self):
        return self.name + " плавает в воде."

    def jump(self):
        return self.name + " делает высокий прыжок."


class ZooShow:
    def __init__(self):
        self.reptiles = [
            Reptile("Гена", 3, 12.0, "Питон", "мыши", "гладкая", False),
            Reptile("Тортила", 5, 25.0, "Варан", "мясо", "твердая", True)
        ]
        self.amphibians = [
            Amphibian("Квак", 1, 0.3, "Лягушка", "мошки", "влажная", "высокая"),
            Amphibian("Лунтик", 2, 0.5, "Тритон", "черви", "гладкая", "средняя")
        ]

    def start(self):
        print("Привет! Добро пожаловать в зоошоу!")
        print("Какое шоу хочешь посмотреть?")
        print("1. Пресмыкающиеся")
        print("2. Земноводные")
        
        choice = input("Введи цифру (1 или 2): ").strip()
        
        if choice == "1":
            show_title = "ШОУ ПРЕСМЫКАЮЩИХСЯ"
        elif choice == "2":
            show_title = "ШОУ ЗЕМНОВОДНЫХ"
        else:
            print("Эм, такого варианта нет, пусть будут пресмыкающиеся.")
            show_title = "ШОУ ПРЕСМЫКАЮЩИХСЯ"

        print("\nВыбери билет на шоу:")
        print("1. Обычное место (500 руб.)")
        print("2. ВИП-место (1500 руб.)")
        
        ticket = input("Твой выбор (1 или 2): ").strip()
        
        if ticket == "2":
            seat = "ВИП-место"
            price = "1500 руб."
        else:
            seat = "Обычное место"
            price = "500 руб."

        print("\n" + "~" * 40)
        print("Ты взял билет: " + seat + ", цена: " + price)
        print("\"" + show_title + "\"")
        print("они будут делать сальто на шаре и кататься на велике")
        print("~" * 40)


if __name__ == "__main__":
    show = ZooShow()
    show.start()