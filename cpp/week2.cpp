#include <iostream>
#include <string>


bool checkAnagram(std::string &word1, std::string &word2);




int main(){
    std::string word1;
    std::string word2;

    std::cin >> "Insert first word: " >> word1;
    std::cin >> "Insert second word: " >> word2;

    if(word1 == word2){
        std::cout << "Same words are not anagrams";
        return 0;
    }



    return 0;
}


bool checkAnagram(std::string &word1, std::string &word2){
    char abc[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 
                        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
                    'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'};

    for(int i = 0; i < 26; i++) {

    }
    
}

size_t countOccurrences(char c, std::string &str)
{
    size_t count = 0;
    char tmp = static_cast<char>(tolower(static_cast<unsigned char>(c)));

    for (char i : str)
        if (tolower(static_cast<unsigned char>(i)) == tmp)
            count++;

    return count;
}
