#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int setup() {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
}

int func() {
    char user[0x10] = "user";
    char buf[0x10];

    printf("Hello, what's your name?\n");
    fgets(buf, 0x1C, stdin);
    printf("Hello %s\n", buf);
    if (!strncmp(user, "sudo", 4)) {
        printf("Good job! Here is your flag:\n");
        system("cat flag.txt");
    } else {
        printf("You do not have permission!\n");
    }
    return 0;
}

int main() {
    setup();
    func();
}