#ifndef STL_EXAMPLES_H_
#define STL_EXAMPLES_H_
#include <vector>
#include <iostream>
#include <string>

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

void move_backwards_example()
{

    message("move_backwards example");

    {
        std::string elems[10] = {"air","water","fire","earth"};
        std::cout << "elems contains:";
        for (int i=0; i<10; ++i)
            std::cout << " [" << elems[i] << "]";
        std::cout << '\n';

        std::move_backward(elems,elems+4,elems+5);
        std::cout<< "back" << std::endl;
        std::cout << "elems contains:";
        for (int i=0; i<10; ++i)
            std::cout << " [" << elems[i] << "]";
        std::cout << '\n';

    }
    std::cout<< "   " << std::endl;
    {
        std::string elems[10] = {"air","water","fire","earth"};
        std::cout << "elems contains:";
        for (int i=0; i<10; ++i)
            std::cout << " [" << elems[i] << "]";
        std::cout << '\n';


        std::move_backward(elems,elems+1,elems+2);
        std::cout<< "swap" << std::endl;
        std::cout << "elems contains:";
        for (int i=0; i<10; ++i)
            std::cout << " [" << elems[i] << "]";
        std::cout << '\n';
    }
    std::cout<< "   " << std::endl;
    {
         std::string elems[10] = {"0","1","2"};
        std::cout << "elems contains:";
        for (int i=0; i<10; ++i)
            std::cout << " [" << elems[i] << "]";
        std::cout << '\n';


        std::move_backward(elems,elems+1,elems+2);
        std::cout<< "move_back" << std::endl;
        std::cout << "elems contains:";
        for (int i=0; i<10; ++i)
            std::cout << " [" << elems[i] << "]";
        std::cout << '\n';
    }

}

void move_example()
{

    message("move example");

    std::vector<int> v1 = {{0,1,2,3,4}};
    std::vector<int> v2(v1.size());

    v2 = std::move(v1);

    message("v1");
    print(v1);
    message("v2");
    print(v2);
}

void swap_example()
{

    message("swap example");

    std::vector<int> v1 = {{0,1,2,3,4}};
    std::vector<int> v2 = {{5,6,7,8,9}};

    std::swap(v1,v2);

    message("v1");
    print(v1);
    message("v2");
    print(v2);
}



#endif
