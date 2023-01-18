// fizzBuzz

function range(to, from=0)
{
    for (let i = from; i < to; i++) 
    {
        if(i % 3 == 0 && i % 5 == 0){
            console.log(i, "FizzBuzz");
        }    
        else if (i % 3 == 0){
            console.log(i, "Fizz");
        }
        else if(i%5 == 0)
        {
            console.log(i, "Buzz")
        }
    }
}

range(100)
