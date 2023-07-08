class Police:
    



    def __init__(self, health, ammo):
        self.health = health
        self.ammo = ammo

    def add_ammo(self):
        self.ammo += 200

        
    #setter
    def set_new_var(self, *args, **kwargs):
        self.new_var = 200



obj = Police(100,200)

# print(obj.health)

obj2 = Police(100,300)
print(obj2.ammo)
obj2.add_ammo()
obj2.set_new_var()
print(obj2.ammo)
print(obj2.new_var)




# def abc(*args, **kwargs):
# #     print(*kwargs)

# abc(a=2)