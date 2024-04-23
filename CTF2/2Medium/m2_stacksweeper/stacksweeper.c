#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int setup() {   
    setbuf(stdin, 0);
    setbuf(stdout, 0);
}

int win() {
    char* argv[3] = {"/bin/cat", "flag.txt", NULL};
    printf("Good job!\n");
    execve("/bin/cat", argv, NULL);
}

int main() {
    setup();
    char flag3[0x10] = "[REDACTED]";
    char mine3[0x10] = "[REDACTED]";
    char mine2[0x10] = "[REDACTED]";
    char flag2[0x10] = "[REDACTED]";
    char mine[0x10] = "[REDACTED]";
    char flag[0x10] = "[REDACTED]";
    char input[0x10] = "";

    printf("\033[0;93m");
    printf("Welcome to the stacksweeper!\n");
    printf("I seem to have forgotten where I placed my mines...\n");
    printf("Will you be able to avoid all the mines and match all the flags?\n");
    printf("Please enter your input: ");
    gets(input);
    printf("\n");

    if (strncmp(input, flag, 0x10)) {
        printf("\033[0;31mInput does not match flag, you stepped on a landmine!\033[0;39m\n");
        exit(1);
    }

    if (strncmp(mine, "BLzxU21EHIUoVg2s", 16)) {
        printf("\033[0;31mYou stepped on mine #1!\033[0;39m\n");
        exit(1);
    }

    if (strncmp(input, flag2, 0x10)) {
        printf("\033[0;31mInput does not match flag 2, you stepped on a landmine!\033[0;39m\n");
        exit(1);
    }

    if (strncmp(mine2, "IYMexlnYF5v2Zj2c", 16)) {
        printf("\033[0;31mYou stepped on mine #2!\033[0;39m\n");
        exit(1);
    }

    if (strncmp(mine3, "VYbnQCgGYTmvzd3H", 16)) {
        printf("\033[0;31mYou stepped on mine #3!\033[0;39m\n");
        exit(1);
    }

    if (strncmp(input, flag3, 0x10)) {
        printf("\033[0;31mInput does not match flag 3, you stepped on a landmine!\033[0;39m\n");
        exit(1);
    }
}