from permutation import permutate

#main function
def path_count(x, y):
	#x axis is represented by "E"(east) and y axis is represented by "N"(north)
	string = ""
	for i in range(x):
		string += "E"
	for i in range(y):
		string += "N"

	#permutation of the string	
	p_object = permutate()
	total_possible_path = p_object.get_elements(string, len(string))
	total_valid_path = 0
	
	#to caculate total number of valid path
	for path in total_possible_path:
		#checking for 3 steps
		E_count = 0
		N_count = 0
		valid_path = True
		for i in path:
			if i == "E":
				if N_count == 3:
					valid_path = False
					break
				if E_count == 0:
					N_count = 0
				E_count +=1

			if i== "N":
				if E_count == 3:
					valid_path = False
					break
				if N_count == 0:
					E_count = 0

				N_count += 1

		if N_count == 3:
			valid_path = False

		if E_count == 3:
			valid_path = False

		if valid_path == True:
			total_valid_path += 1

	return total_valid_path

#take user inputs, and print the output
if __name__ == "__main__":
	x = int(input("enter coordinate of X axis : "))
	y = int(input("enter coordinate of Y axis : "))
	#calling main function
	total_valid_path = path_count(x,y)

	print("Never 3 steps\nWe never take except 3 steps in same direction :)")
	print(f"Total valid path is {total_valid_path}")