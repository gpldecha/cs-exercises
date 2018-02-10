#ifndef INSERTION_SORT_H_
#define INSERTION_SORT_H_

#include <bits/stl_iterator_base_types.h>
#include <utility>
#include <functional>
#include <algorithm>
#include <iostream>
#include <assert.h>


template<typename T>
void print(T& input)
{
    for (auto const& c : input)
        std::cout << c << ' ';
    std::cout<<std::endl;
}

void print_vec(std::vector<int>& input)
{
    for (auto const& c : input)
        std::cout << c << ' ';
    std::cout<<std::endl;
}

void message(std::string msg)
{
    std::cout<< msg << std::endl;
}

namespace sort{

template<typename _RandomAccessIterator>
double sum(_RandomAccessIterator __first, _RandomAccessIterator __last)
{
    double val = 0;
    if (__first == __last) return val;
    for (_RandomAccessIterator __i = __first; __i != __last; ++__i)
    {
        val += *__i;
    }

    return val;
}

template<typename _RandomAccessIterator>
void print(_RandomAccessIterator __first, _RandomAccessIterator __last)
{
    for (_RandomAccessIterator __i = __first; __i != __last; ++__i)
    {
        std::cout<< *__i << " ";
    }
    std::cout<<std::endl;
}


template<typename _RandomAccessIterator, typename _Compare>
void unguarded_linear_insert(_RandomAccessIterator __last, _Compare __comp){

    typename std::iterator_traits<_RandomAccessIterator>::value_type
            __val = std::move(*__last);

    _RandomAccessIterator __next = __last;
    --__next;
    while (__comp(__val, __next))
    {
        *__last = std::move(*__next);
        __last = __next;
        --__next;
    }
    *__last = std::move(__val);
}


template<typename _RandomAccessIterator,typename _Compare>
void insertion(_RandomAccessIterator __first, _RandomAccessIterator __last,_Compare __comp){

    _RandomAccessIterator __i = __first;

    if (__i == __last) return;

    for (_RandomAccessIterator __j = __i + 1; __j != __last; ++__j)
    {

        if (*__j < *__i)
        {
            std::cout<< *__j << " < " << *__i << std::endl;
            typename std::iterator_traits<_RandomAccessIterator>::value_type
                    __val = std::move(*__j);
                            //std::move_backward(__i, __j, __j + 1);
                            std::swap(__i,__j);
                    //*__i  = std::move(__val);
        }else{
            std::cout<< *__j << " >= " << *__i << std::endl;
            std::__unguarded_linear_insert(__j,__gnu_cxx::__ops::__val_comp_iter(__comp));
        }
        print(__first,__last); std::cout<< std::endl;

    }
}

void swap(std::size_t i, std::size_t j, std::vector<int>& vec)
{
    assert( i < vec.size() );
    assert( j < vec.size() );


    int tmp = vec[i];

    vec[i]  = vec[j];
    vec[j]  = tmp;
}

void insertion_simple(std::vector<int>& a)
{
    std::size_t j;
    for(std::size_t i = 1; i < a.size();i++)
    {
        j = i;
        while( (j > 0) && (a[j] < a[j-1]) )
        {
            swap(j,j-1,a);
            j = j - 1;
        }
    }
}




}


#endif
