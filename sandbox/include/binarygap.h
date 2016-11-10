#ifndef BINARYGAP_H_
#define BINARYGAP_H_

#include <bitset>
#include <string>
#include <iostream>


//
int binarygap_solution(int N){
/* N -> string 1001110001
 * find max gap
 *
 * */
    std::string binary = std::bitset<64>(N).to_string(); //to binary
    int first_non_zero = binary.find("1");
    binary = binary.substr(first_non_zero,binary.size()-first_non_zero);

    std::cout<< "binary: " << binary << std::endl;

    // count gaps
    int max_gap     = 0;
    int current_gap = 0;
    for(int i = 1; i < binary.size();i++)
    {
        if(binary[i] != '1')
        {
            current_gap++;
        }else{
            if(current_gap > max_gap){
                max_gap = current_gap ;
            }
            current_gap = 0;
        }

    }

    if(current_gap > max_gap){
        max_gap = current_gap ;
    }

    return max_gap;
}

void test_binarygap_solution()
{

    //https://codility.com/programmers/lessons/1-iterations/binary_gap/
    std::cout<< "gap: " << binarygap_solution(529) << std::endl;

    std::cout<< "gap: " << binarygap_solution(20) << std::endl;


}



#endif
