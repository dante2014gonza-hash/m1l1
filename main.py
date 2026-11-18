import random

ñassword = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

contraseña = int(input("intrudusca su conchaseña :3"))

password = ""

for i in range(contraseña):
    password = password  + random.choice(ñassword)

print(password)
