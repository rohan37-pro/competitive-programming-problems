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

		#generating the permutation list
		for i in range(possible_combination):
			#generate a random combination
			self.generate_random_list()
			if i!=0:
				#check if the generated random list is in the permutation list or not
				while self.check_list_in_2Dlist():
					self.generate_random_list()
			self.permutation_list.append(self.temp_random_list)

		#return the final permutation list
		return self.permutation_list

	#to find the factorial of a number
	def factorial(self, num):
		fact = 1
		for i in range(1,num+1):
			fact *= i
		
		return fact


	#function to generate a random list
	def generate_random_list(self):
		temp_index_list = []
		for i in range(self.r):
			#a random number to generate random list
			temp_random = random.randint(0, self.length_of_string-1)
			#checking if the random number is already in the list or not
			while temp_random in temp_index_list:
				temp_random = random.randint(0, self.length_of_string-1)
			temp_index_list.append(temp_random)

		#append the values according to the generated random list
		self.temp_random_list = []
		for i in range(self.r):
			self.temp_random_list.append(self.string[temp_index_list[i]])


	#function to check the random list is already in the permutation list or not
	def check_list_in_2Dlist(self):
		check_list = []
		for i in range(len(self.permutation_list)):
			check = 1
			for j in range(self.r):
				#comparing individual values
				if self.permutation_list[i][j] == self.temp_random_list[j]:
					check = check and 1
				else:
					check = check and 0
			check_list.append(check)

		check = 0
		for i in check_list:
			check = check or i

		return check


	#a function that will return the total number of possible permutations.
	def apply_formula(self):
		#formula of permutation
		comb = int(self.factorial(self.length_of_string)/self.factorial(self.length_of_string - self.r))
		#formula of permutation for multiple occurance of same character
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