#ifndef OCADO_H_
#define OCADO_H_

#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <map>

bool myfunction (int i,int j) { return (i<j); }

int solution_ex1(std::vector<int> &A) {
    // write your code in C++11 (g++ 4.8.2)

    // sanitise input
    if(A.size() == 0 || A.size() > 100000){
        return -1;
    }

    // sort array O(N log N)
    std::sort(A.begin(), A.end());

    // debug
    for(int i = 0; i < A.size(); i++)
    {
     std::cout<< A[i] << " ";
    }

    int N       = A.size();
    int median  = 0;
    int idx     = 0;

    if( N % 2 == 0)
    {
        // even
        idx = N/2;
    }else{
        // odd
        idx = (N-1)/2;
    }

    median = A[idx];


    return median;
}


int solution_ex2(std::vector<int>& A)
{
    // sanitise input
    if(A.size() == 0)
        return -1;

    // finds the most freequently occuring
    std::map<int,int> map_A;
    std::map<int,int>::iterator it;
    map_A.insert(std::pair<int,int>(A[0],1));


    for(int i = 1; i < A.size();i++){
        // check if number exists
        it = map_A.find(A[i]); // log(N)
        if (it != map_A.end()){ // it exists
                it->second = it->second + 1;
        }else{
            map_A.insert(std::pair<int,int>(A[i],1));
        }
    }

    int max = 0;
    int num = 0;
    // find maximum
    for(it=map_A.begin(); it != map_A.end();it++) // O(N)
    {
        std::cout<< it->first << "  " << it->second << std::endl;
        if(it->second > max)
        {
            max = it->second;
            num = it->first;
        }
    }

    return num;
}


class Set{
    public:
    Set(){ length = 0;}
    // check if idx is already in this set, return the length
    // of remaining to travel.
    void push_back(std::size_t idx)
    {
        indices.push_back(idx);
        length = length + 1;
    }

    std::vector<std::size_t> indices;
    std::size_t length;
};

bool is_in_set(const Set& set,const std::size_t idx,std::size_t& length)
{
    std::cout<< "== is_in_set ===" << std::endl;
    for(std::size_t k = 0; k < set.indices.size();k++)
    {
        if(set.indices[k] == idx)
        {
            length = set.indices.size() - k;
            return true;
        }
    }
    return false;
}

bool is_in_sets(const std::vector<Set>& sets,const std::size_t idx,std::size_t& length){
    std::cout<< "sets.size(): " << sets.size() << std::endl;
    for(std::size_t i = 0; i < sets.size();i++){
        if( is_in_set(sets[i],idx,length) )
        {
            return true;
        }
    }
    return false;
}


// cral an array iteratively until end or loops
 Set crall_indices(const std::vector<int>& A,const std::size_t idx, std::vector<Set>& sets)
{
    // creat an new set for this idx

    Set set;
    set.indices.push_back(idx);
    std::size_t length = 0;

    std::cout<< "idx: " << idx << std::endl;
    int count = 0;
    for(std::size_t i = A[idx]; i < A.size(); i = A[i])
    {
        std::cout<< "  i: " << i << std::endl;
        // check if i is in other sets
        if(is_in_sets(sets,i,length))
        {
            std::cout<< "is in set" << std::endl;
            // i is already in another set
            set.length = set.length + length;
            return set;
        }else{
            // i is not
            std::cout<< "is not in set" << std::endl;
            set.push_back(i);

        }
        count++;
        if(count > 3)
            return set;
    }

    return set;
}

void print_set(const Set& set)
{
    for(int i = 0; i < set.indices.size(); i++){
        std::cout<< set.indices[i] << " ";
    }
    std::cout<<std::endl;
}

int solution_ex3(std::vector<int>& A)
{

    std::vector<Set> sets;

    //for(std::size_t i = 0; i < A.size();i++)
    //{

    int i = 0;
    std::cout<< "i " << std::endl;

    Set set = crall_indices(A,i,sets);
    print_set(set);


    //}

    return 0;
}





void test_exercise1()
{
    std::cout<< "==test1==" << std::endl;

    {
        std::cout<< "#1" << std::endl;
        std::vector<int> A = {1, 2, 5, 10, 20, 1};
        solution_ex1(A);
    }

    {
        std::cout<< "#2" << std::endl;
        std::vector<int> A = {1};
        solution_ex1(A);
    }

    {
        std::cout<< "#3" << std::endl;
        std::vector<int> A = {};
        solution_ex1(A);
    }

}


void test_exercise2()
{
    std::cout<< "==test2==" << std::endl;
    {
        std::vector<int> A = {20, 10, 30, 30, 40, 10};
        std::cout<< "ocado example  :  " << solution_ex2(A) << std::endl;
    }

    {
        std::vector<int> A = {20};
        std::cout<< "one entry  :  " << solution_ex2(A) << std::endl;
    }


    {
        std::vector<int> A = {};
        std::cout<< "empty array  :  " << solution_ex2(A) << std::endl;
    }

    {
        std::vector<int> A = {10,20,30,40,50,60,80};
        std::cout<< "no elements are the same  :  " << solution_ex2(A) << std::endl;
    }


}


void test_exercise3()
{
    std::cout<< "==test3==" << std::endl;
    std::cout<< " find greatest set " << std::endl;
    {

        std::vector<int> A = {5,4,0,3,1,5,6};

        solution_ex3(A);


    }


}


#endif
