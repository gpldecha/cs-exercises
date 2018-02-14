#include "insertion_sort.h"
#include "merge_sort.h"
#include "heapsort.h"

#include <vector>
#include <iostream>
#include <algorithm>

bool less_than (int i,int j) { return (i<j); }

void merge_sort_example(){
  std::vector<int> input = {5,4,3,2,1,0};
  message("merge sort");
  merge_sort<int>::sort(&input[0],input.size(),less_than);
  print(input);
}

void construct_heap()
{
  std::vector<int> arr = {4,5,8,9,11,14,12,10,19,18,20};

  heapsort::to_heap<int>(arr);

  if(heapsort::is_valid_heap<int>(arr))
  {
    std::cout<< "is valid heap: true" << std::endl;
  }else{
    std::cout<< "is valid heap: false" << std::endl;
  }

  for(int value : arr)
  {
    std::cout<< value << std::endl;
  }

}

int main(int argc, char** argv)
{

  // std::vector<int> arr = {20,18,19,10,12,14,11,9,8,5,4};
  std::vector<int> arr = {4,5,8,9,11,14,12,10,19,18,20};

  heapsort::sort<int>(arr);

  for(int value : arr)
  {
    std::cout<< value << std::endl;
  }




	return 0;
}
