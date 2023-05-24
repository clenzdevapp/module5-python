
def test():
    return "Hallo Welt"


test()


print("There are {n:d} states in the USA".format(n=50))


my_dict = {1: 2, True: 3, "Hallo": 5}


print(my_dict[True])


dict(((3, 4), (True, False)))


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 101010]
print(my_list[0:-2])
print(my_list[::2])


a = 700
print(id(a))


seq = 'GACAGACUCCAUGCACGUGGGUAUCUGUC'
for i in range(2, 10, 2):
    print(i, end='    ')

for i, base in enumerate(seq):
    if base in "Gg":
        print(i, end="    ")


# Parallele Schleifenausgabe
names = ('Dunn', 'Ertz', 'Lavelle', 'Rapinoe')
positions = ('D', 'MF', 'MF', 'F')
numbers = (19, 8, 16, 15)

for num, pos, name in zip(numbers, positions, names):
    print(num, name, pos)


# print?


my_tuple = (2, 36, 12)
my_list = [1, 3, 2]
my_dict = {"a": 2, "b": 3, "c": 4}


def my_function(a, b, c):
    return a**2, b**2, c**2


print(my_function(*my_tuple))
print(my_function(*my_list))
print(my_function(**my_dict))


# Define sequence
seq = 'GACAGACUCCAUGCACGUGGGUAUCAUGUC'

# Count G's and C's
print(seq.count('G') + seq.count('C'))
