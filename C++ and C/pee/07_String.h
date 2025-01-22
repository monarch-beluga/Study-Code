#include<string>
using namespace std;

int Index(string S, string T){
	int i = 0, j = 0;
	while(i < S.length() && j < T.length()){
		if(S[i] == T[j]){
			i++;
			j++;
		}
		else{
			i = i - j + 1;
			j = 0;
		}
	}
	if(j >= T.length())
		return i - T.length();
	else
		return -1;
}

int* get_next(string T){
	int *next = new int[T.length()];
	int i = 0, j = -1;
	next[0] = -1;
	while(i < T.length()){
		if(j == -1 || T[i] == T[j]){
			++i;
			++j;
			next[i] = j;
		}
		else
			j = next[j];
	}
	return next;
}

