import random
from time import sleep

class permutate:

	#this is our main function which will return the permutate 2D list
	def get_elements(self, string, r):
		self.string = string
		self.r = r
		self.length_of_string = len(string)
		self.permutation_list = []
		#formula of permutaion
		possible_combination = self.apply_formula()
		#print(f"possible_combination : {possible_combination}")

		for i in range(possible_combination):
			self.generate_random_list()
			#print(f"temp_random_list : {self.temp_random_list}")
			if i!=0:
				while self.check_list_in_2Dlist():
					#print(f"{self.temp_random_list} is in {self.permutation_list}")
					self.generate_random_list()
			self.permutation_list.append(self.temp_random_list)

		#print(f"permutation_list - {self.permutation_list}")
		return self.permutation_list


	def factorial(self, num):
		fact = 1
		for i in range(1,num+1):
			fact *= i
		
		return fact


	def generate_random_list(self):
		temp_index_list = []
		for i in range(self.r):
			temp_random = random.randint(0, self.length_of_string-1)
			while temp_random in temp_index_list:
				temp_random = random.randint(0, self.length_of_string-1)
			temp_index_list.append(temp_random)

		self.temp_random_list = []
		for i in range(self.r):
			self.temp_random_list.append(self.string[temp_index_list[i]])
		#print(f"temp_random_list = {self.temp_random_list}")


	def check_list_in_2Dlist(self):
		check_list = []
		#print(f"checking list \n{self.temp_random_list} \nin list \n{self.permutation_list}")
		for i in range(len(self.permutation_list)):
			check = 1
			for j in range(self.r):
				#print(f"self.permutation_list[{i}] - {self.permutation_list[i]}")
				#print(f"self.permutation_list[{i}][{j}] - {self.permutation_list[i][j]}")
				if self.permutation_list[i][j] == self.temp_random_list[j]:
					check = check and 1
				else:
					check = check and 0
					#print(f"{self.permutation_list[i][j]} and {self.temp_random_list[j]} didn't match, ",end=' ')
			check_list.append(check)
			#print("")

		check = 0
		for i in check_list:
			check = check or i

		#print(f"check result - {check}\n")
		return check

	def apply_formula(self):
		comb = int(self.factorial(self.length_of_string)/self.factorial(self.length_of_string - self.r))
		string_dic = {}
		for i in self.string:
			string_dic[i] = self.string.count(i)
		for i in string_dic:
			comb /= self.factorial(string_dic[i])

		return int(comb)

'''
if __name__ == "__main__":
	string = input("enter a string : ")
	r = int(input("enter value of r : "))
	print("the permutations are ")
	lis = permutate()
	lis = lis.get_elements(string,r)
	for i in lis:
		print(i)
'''