/*
Make a program that detects whether a number is prime or not.
*/ 

#include <iostream>

bool is_prime(int);

int main() 
{
    int number;

    std::cout << "This program will tell you whether the number you enter is prime or not." << std::endl;

    std::cout << "Insert a positive number: ";
    std::cin >> number;
    
    if(is_prime(number))
    {
        std::cout << "Is prime";
    }
    else 
    {
        std::cout << "Not prime.";
    }
    
    return 0;

}

bool is_prime(int number) 
{
    for(int i = 2; i < number; i++) 
    {
        if(number % i == 0) 
        {
            return false;
        }
    }
    return true;
}