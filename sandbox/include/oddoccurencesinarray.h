#ifndef ODDOCCURENCEINARRAY_H_
#define ODDOCCURENCEINARRAY_H_

// all about XOR http://www.cplusplus.com/doc/boolean/
// http://www.ardendertat.com/2011/12/13/programming-interview-questions-22-find-odd-occurring-element/
#include <iostream>

int odd_occurence_in_array(int A[], int N){
    int odd_occ = A[0];
    for(int i = 1; i < N; i++)
    {
        odd_occ = odd_occ^A[i];
    }
    return odd_occ;
}

void test_odd_occ()
{

    {
        int A[] = {1, 2, 3, 1, 2, 3, 1};
        std::cout<< "start" << std::endl;
        std::cout<< "odd_occurence_in_array: " << odd_occurence_in_array(A,7) << std::endl;
    }
    {
        int A[] = {9,3,9,3,9,7,9};
        std::cout<< "start" << std::endl;
        std::cout<< "odd_occurence_in_array: " << odd_occurence_in_array(A,7) << std::endl;
    }
}



#endif
