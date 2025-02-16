#include <iostream>
#include <cstdlib>

int main() {
    srand(time(0));
    int sunshine = rand() % 100;
    if (sunshine > 50) {
        std::cout << "It's a sunny day in the office! ☀️" << std::endl;
    } else {
        std::cout << "Rainy day? Let's pretend it's sunny! 🌧️" << std::endl;
    }
    
    std::cout << "Generated random code... don't ask why! 🤖" << std::endl;
    for (int i = 0; i < 5; ++i) {
        std::cout << "Random number: " << rand() % 100 << " - Stay hydrated! 💧" << std::endl;
    }
    return 0;
}