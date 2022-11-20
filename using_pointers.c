#include <stdio.h>

int str_comp(char* s1, char* s2) {
	while(*s1 != 0 && s2 != 0)
		if(*s1++ != *s2++)
			return 0;
	return *s1 == *s2;
}

int main(void) {
	printf("d: %d", str_comp("abc", "acb"));
}
