'''
class Rec:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    default_color = "green"

print(Rec.default_color)
recta_1 = Rec(5,8)
print(f"{recta_1.w}, {recta_1.h}")

self.role = role
'''
class Guest:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get_describ_name(self):
        long_name = f"{self.name}, г. {self.city}"
        return long_name.title()

class RoleG(Guest):
    def __init__(self, name, city):
        super().__init__(name, city)
        self.role = "наставник"

    def show_role(self):
        role_user = f"'{self.role}'"
        return role_user.title()


guest_1 = RoleG("иван петров", "москва")

print(guest_1.get_describ_name(), guest_1.show_role())
#print(guest_1.show_role())
