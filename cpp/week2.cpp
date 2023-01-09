#include <iostream>
#include <string>


bool checkAnagram(std::string &word1, std::string &word2);
size_t countOccurrences(char c, std::string &str);



int main(){
    std::string word1;
    std::string word2;


    std::cout << "Insert the first word: ";
    std::cin >>  word1;
    std::cout << "Insert the second one: ";
    std::cin >>  word2;


    if(word1 == word2){
        std::cout << "Same words are not anagrams";
        return 0;
    }

    if (checkAnagram(word1, word2)){
        std::cout << "They are anagrams" << std::endl;
    } else
    {
        std::cout << "Not anagram" << std::endl;
    }

    return 0;
}


bool checkAnagram(std::string &word1, std::string &word2){
    char abc[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
                        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'};
    int occurrencesA, occurrencesB;

    for(int i = 0; i < 26; i++) {
        occurrencesA = countOccurrences(abc[i], word1);
        occurrencesB = countOccurrences(abc[i], word2);
        if(occurrencesA != occurrencesB){
            return false;
        }
    }

    return true;

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

