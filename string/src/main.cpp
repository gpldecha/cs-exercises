#include "mirror.h"
#include <iostream>

int main(int argc, char** argv){



    std::string s = "lVHt\nJVhv\nCSbg\nyeCt";
    std::string sol = "yeCt\nCSbg\nJVhv\nlVHt";

    std::string output = Mirror::horMirror(s);

    std::cout<< output << std::endl;

    if(output == sol)
    {
        std::cout<< "Correct" << std::endl;
    }else{
        std::cout<< "InCorrect" << std::endl;
    }


	return 0;
}
