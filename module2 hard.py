
import random
def find_password(n):
    password = ""
    for i in range(1, n):
        for j in range(1, i):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

random_num = random.randint(3,20)
print(f"Число на первой табличке: {random_num}")
print(find_password(random_num))
