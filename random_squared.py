import random

random_number_list = []
run = True


def generate_Num():
	global random_number_list
	global run
	if len(random_number_list) < 20:
		random_number_list.append(random.randint(0,49))
		print(random_number_list)
	else:
		run = False
		square_the_num()


def square_the_num():
	global random_number_list
	squared_num = [j**2 for j in random_number_list]
	print(squared_num)


while run:
	generate_Num()