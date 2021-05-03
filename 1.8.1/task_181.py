class Cat:
    def __init__(self, sex, name, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

cat_1 = Cat("Барон", "кот", 2)
cat_2 = Cat("Сэм", "кот", 2)

print(cat_1.get_name(), cat_1.get_sex(), cat_1.get_age())
print(cat_2.get_name(), cat_2.get_sex(), cat_2.get_age())
