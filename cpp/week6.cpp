/*
Reverse a string
*/

#include <iostream>
#include <string>

int main() 
{
    std::string::reverse_iterator loop;
    std::string textLine;


    std::getline(std::cin,textLine);

    for(loop = textLine.rbegin(); loop != textLine.rend(); loop++)
    {
        std::cout << *loop;
    }
    
    return 0;
}
