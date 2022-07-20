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

		for i in range(possible_combination):
			self.generate_random_list()
			#print(f"temp_random_list : {self.temp_random_list}")
			if i!=0:
				while self.check_list_in_2Dlist():
					#print(f"{self.temp_random_list} is in {self.permutation_list}")
					self.generate_random_list()
			self.permutation_list.append(self.temp_random_list)

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
		check = 1
		for i in range(len(self.permutation_list)):
			for j in range(self.r):
				if self.permutation_list[i][j] == self.temp_random_list[j]:
					check = check and 1
				else:
					check = check and 0

		return check

	def apply_formula(self):
		possible_combination = int(self.factorial(self.length_of_string)/self.factorial(self.length_of_string - self.r))
		string_dic = {}
		for i in self.string:
			string_dic[i] = self.string.count(i)
		for i in string_dic:
			possible_combination /= self.factorial(string_dic[i])

		return int(possible_combination)

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