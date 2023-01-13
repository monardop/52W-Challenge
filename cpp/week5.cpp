/*
A program that, based on the sides entered 
:return: the type of figure and its area.
*/

#include <iostream>

float triangle();
float square();
float rectangle();

// I'm going to use a function pointer since none of the three take arguments
float (*figure[3])(void) = {triangle, square, rectangle};

int main()
{
    int selection;
    float value;

    // I'm assuming that the selection will be correct
    std::cout << "Main menu:\n" << "0- Triangle\n" << "1- Square\n" << "2- Rectangle\n";
    std::cin >> selection; 
    value = figure[selection]();
    std::cout << "The area is: " << value << "u2";

    return 0;
}

float triangle() 
{
    float base, height;

    std::cout << "Set the base: ";
    std::cin >> base;
    std::cout << "Set the height: "; 
    std::cin >> height;

    return (base * height)/2;
}

float square()
{
    float side;

    std::cout << "Set the sides lenght: ";
    std::cin >> side;

    return (side * side);
}

float rectangle()
{
    float width, height;

    std::cout << "Set the width: ";
    std::cin >> width;
    std::cout << "Set the height: "; 
    std::cin >> height;

    return (width * height);
}