#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 80

int main() {
    char line[MAX_LINE_LENGTH] = {0};
    FILE *file = fopen("flag.txt", "r");
    if(!file) return EXIT_FAILURE;
    fgets(line, MAX_LINE_LENGTH, file);
    fclose(file);

    int key = 16*3-4+3-4/2-40;

    for(int i=0; line[i] != 0; i++) {
        char c = line[i];
        if(isalpha(c)) {
            if (isupper(c)){line[i] = (c - 'A' + key) % 26 + 'A';}
            else {line[i] = (c - 'a' + key) % 26 + 'a';}} 
        else if (isdigit(c)) {line[i] = (c - '0' + key) % 10 + '0';}
        else {}
    }
    file = fopen("caesar.txt", "w");
    fwrite(line, 1, sizeof(line), file);
    fclose(file);
}