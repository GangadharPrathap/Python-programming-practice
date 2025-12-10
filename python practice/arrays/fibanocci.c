#include<stdio.h>

void printFibonacci(int n) {
    int a = 0, b = 1, next;

    for (int i = 0; i < n; i++) {
        printf("%d", a);
        if (i < n - 1) printf(" ");
        next = a + b;
        a = b;
        b = next;
    }
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 1;

    if (n < 1) n = 1;
    if (n > 50) n = 50;

    printFibonacci(n);
    return 0;
}