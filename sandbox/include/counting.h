#ifndef COUNTING_H_
#define COUNTING_H_

#include <vector>

bool is_permutation(std::vector<int> &A)
{

    int max, min, sum;
    max = A[0]; min = A[0]; sum = 0;
    // 1..1,000,000,000
    // get sum
    int N = A.size();
    for(int i = 0; i < N; i++)
    {
        sum = sum + A[i];
        if(A[i] > max){
            max = A[i];
        }
        if(A[i] < min)
        {
            min = A[i];
        }
    }
    int val = (static_cast<double>(min + max)/2.0) * static_cast<double>(N);

    if(static_cast<int>(val) != sum)
    {
        return false;
    }else{
        return true;
    }
}

void test_permutation()
{

    {
        std::vector<int> A = {4,1,3,2};
        std::cout<< "test_permutation(1): " << is_permutation(A) << std::endl;
    }

    {
        std::vector<int> A = {4,1,3};
        std::cout<< "test_permutation(2): " << is_permutation(A) << std::endl;
    }
}


#endif
