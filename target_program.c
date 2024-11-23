#include <stdio.h>
#include <string.h>

void check_access(char *input) {
    // Define a "secret" string that the user must match
    const char *secret = "secret123";

    // Compare the input with the secret string
    if (strcmp(input, secret) == 0) {
        printf("Access granted!\n");
    } else {
        printf("Access denied.\n");
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    check_access(argv[1]);
    return 0;
}
