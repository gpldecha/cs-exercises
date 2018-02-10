#ifndef CS_EXAMPLE_UTILS_H_
#define CS_EXAMPLE_UTILS_H_

#include <iostream>
#include <string>

namespace util{

template<typename T>
void print(const T& input)
{
    for (auto const& c : input)
        std::cout << c << ' ';
    std::cout<<std::endl;
}

void message(std::string msg)
{
    std::cout<< msg << std::endl;
}

}


#endif
