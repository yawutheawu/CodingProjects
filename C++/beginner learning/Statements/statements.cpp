#include <iostream>

int main() {
    std::cout << "Hello\n";
    printf("Hello 1.5\n");
    std::cout << "Hello 2\n";
    std::cout << "The final statement\n";
    printf("Input a thing: ");
    std::string n = "Hello";
    std::cin >> n;
    std::cout << n;
}