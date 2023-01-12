/*
This module will have the function of storing validations and other types of functions that are necessary and that do not come by default in the standard library.
*/
#include "utilities.h"

int validInput(int least, int greatest)
{
    int input;
    do
    {
      std::cout << "Insert a number between" << least << " and " << greatest << ": ";
      std::cin >> input;  
    } while (least < input && input < greatest);
    
    return input;
}

int positiveNumber()
{
    int input;
    do
    {
        std::cout << "Insert a positive number: ";
        std::cin >> input;
    } while (input > 0);
    
    return input;
}
