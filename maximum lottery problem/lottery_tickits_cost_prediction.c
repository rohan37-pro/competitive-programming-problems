#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int factorial(int num){
	int fact = 1;
	for (int i=1;i<=num;i++){
		fact *= i;
	}
	return fact;
}

int random(int lower, int upper){
	int random_number;
	random_number = lower+ (rand()%(upper-lower+1));
	return random_number;

}

int check_num(int len, int array[], int num){
	int element_present = 0;
	for (int i=0; i<len; i++){
		if (array[i] == num){
			element_present = 1;
			break;
		}
	}
	if (element_present==1){
		return 1;
	}
	else{
		return 0;
	}
}

int find_greatest(int array[], int len){
	int greatest = 0;
	for (int i=0; i<len; i++){
		if (array[i]>greatest){
			//printf("array[%d] in find_greatest %d\n",i,array[i]);
			greatest = array[i];
			
		}
		//printf("array[%d] in find_greatest %d\n",i,array[i]);
	}
	return greatest;
}

float avarage_of_num(int array[],int len){
	float avarage = 0;
	for (int i=0;i<len; i++){
		avarage += array[i];
	}
	avarage/=len;
	return avarage;
}

int main()
{
	int input;
	int total_balls,inx;
	int comb,r;

	printf("enter total number of balls : ");
	scanf("%d",&total_balls);
	int array[total_balls];

	for (int i=0; i<total_balls; i++){
		printf("enter lottery amount %d : ",i+1);
		scanf("%d",&input);
		array[i] = input;
	}
	printf("enter number of choosing object from the set : ");
	scanf("%d",&r);
	comb = factorial(total_balls)/(factorial(r)*factorial(total_balls-r));
	printf("number of combination is %d\n",comb);
	comb *= total_balls;

	int list_winnings[comb+1];
	double avarage;
	int random_number;
	srand(time(0));

	for (int i=0; i<comb; i++){
		int win;
		avarage = 0;
		int list_random[r];
		for (int j=0;j<r;j++){
			random_number = random(0,total_balls-1);
			if (j!=0){
				while (check_num(j+1,list_random,array[random_number])){
					random_number = random(0,total_balls-1);
				}
			}
			//printf("random number %d\n",random_number);
			list_random[j] = array[random_number];
			avarage += array[random_number];
		}
		win = find_greatest(list_random,r);
		//printf("winning is %d\n",win);
		//printf("avarage is %f\n",avarage);
		list_winnings[i] = win;

	}
	avarage = avarage_of_num(list_winnings, comb);
	float greatest = find_greatest(list_winnings,comb);

	printf("the profitable cost is greater then %f",avarage);
}