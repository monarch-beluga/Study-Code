#include <stdio.h>
int main()
{
	int a,b,c;
	for(a = 0;a <= 33;a++)
		for(b = 0;b <= 50;b++)
		{
			c = 100-a-b;
			if(a*3 + b*2 + 0.5*c == 100)
				printf("����%d,����%d,С��%d\n",a,b,c);
		}
	return 0;
}