#include <iostream>
#include "DocumentParser.h"


int main() {
    auto docs = load_csv("/Users/shubhamfufal/Library/Mobile Documents/com~apple~CloudDocs/2ndSemProject/Bot/Data/final.csv");
    std::cout << "Loaded " << docs.size() << " documents." << std::endl;
    if (!docs.empty()){
        std::cout << "First input: " << docs[0].input << std::endl;
        std::cout << "First output: " << docs[0].output << std::endl;
    }
    return 0;
}