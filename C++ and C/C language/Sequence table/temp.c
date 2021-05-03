#include <stdio.h>

int main()
{
	int nums[100];
	int length = 100;
	int i, j;
	for (i = 0; i < 100; ++i)
		nums[i] = i+1;
	while(length > 1)
	{
		printf("这一轮死亡：\n");
		for (i = 0, j = 0; i < length; i++)
		{
			if (i % 2 != 0)
			{
				nums[j] = nums[i];
				j++;
			}
			else
				printf("%d:%d,", i+1, nums[i]);
		}
		length = j;
		printf("还剩下%d人\n", length);
	}
	printf("最后剩下的人为%d号。\n", nums[0]);
	return 0;
}


