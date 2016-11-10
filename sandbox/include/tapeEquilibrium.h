#ifndef TAPEEQUILIBRIUM_H_
#define TAPEEQUILIBRIUM_H_

#include <iostream>
#include <cmath>

// https://codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

int tape_equi(int A[], int N)
{

    int Sa = A[0];
    int Sb = 0;
    for(int i = 1; i < N;i++)
    {
        Sb = Sb + A[i];
    }

    int min = std::abs(Sa - Sb);
    int diff = 0;
    for(int i = 1; i < N-1;i++)
    {

        Sa = Sa + A[i];
        Sb = Sb - A[i];

        diff = std::abs(Sa - Sb);
        if(diff < min)
        {
            min = diff;
        }


    }

    return min;
}

void test_tape_equi()
{
    int A[] = {3,1,2,4,3};

    std::cout<< "tape_equi: " << tape_equi(A,5) << std::endl;

}


#endif
