#include <stdio.h>
#include <string.h>

#define MAGIC_NUMBER 0xDEADBEEF

typedef struct {
    unsigned int magic;
    char directives[2][20];
} config_t;

config_t* read_config(const char *filename) {
    static config_t config;
    FILE *file = fopen(filename, "r");
    if (!file) {
        return NULL;
    }

    // Read the magic number
    if (fread(&config.magic, sizeof(config.magic), 1, file) != 1) {
        fclose(file);
        return NULL;
    }

    // Read the directives
    if (fread(config.directives, sizeof(config.directives), 1, file) != 1) {
        fclose(file);
        return NULL;
    }

    fclose(file);
    return &config;
}

void program_bug() {
    printf("Program bug triggered!\n");
    // Simulate a crash
    *((volatile int*)0) = 0;
}

void set_option(const char *option) {
    printf("Option set to: %s\n", option);
}

void default_action() {
    printf("Default action executed.\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    config_t *config = read_config(argv[1]);
    if (config == NULL) {
        puts("Configuration syntax error");
        return 1;
    }

    if (config->magic != MAGIC_NUMBER) {
        puts("Bad magic number");
        return 2;
    }

    char *directive = config->directives[0];
    if (strcmp(directive, "crashstring") == 0) {
        program_bug();
    } else if (strcmp(directive, "setoption") == 0) {
        set_option(config->directives[1]);
    } else {
        default_action();
    }

    return 0;
}