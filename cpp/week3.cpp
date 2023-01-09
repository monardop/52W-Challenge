/*
Week 3: Fibonacci secuence. A positive integer n is inserted, and the program returns the nth sequence.
*/
#include <iostream>


void fibonacci(int previous, int next, int position)
{
    std::cout << previous << " ";

    if(position == 0){
        return;
    }
    else
    {
        position--;
        return fibonacci(next, previous + next, position);
    }
}

int main()
{
    int number;

    std::cout<< "Insert how many numbers on the Fibonacci series do you want: ";
    std::cin >> number;
    fibonacci(0,1, number);
    
    return 0;
}