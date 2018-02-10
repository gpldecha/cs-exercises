#include <vector>
#include <algorithm>

namespace heapsort{

template<typename T>
bool is_valid_heap(std::vector<T>& arr)
{
  int num_elem = arr.size();
  int k = 1;
  while(k < num_elem-2)
  {
      if(2*k > num_elem)
        return true;
      if(arr[k-1] < arr[2*k-1])
        return false;
      if(2*k+1 > num_elem)
        return true;
      if(arr[k-1] < arr[2*k+1-1])
        return false;
      k++;
  }
  return true;
}

template<typename T>
void sink(std::vector<T>& arr, int k, int num_elem)
{
    int j = 0;
    while ( k < num_elem )
    {
      j = 2*k;

      // find the biggest child
      if(j+1 <= num_elem){
        if(arr[j+1-1] > arr[j-1])
          j++;
      }

      // compare the biggest child with parent
      if(j <= num_elem && arr[k-1] < arr[j-1]){
        std::swap(arr[k-1], arr[j-1]); k=j;
      }else{
        break;
      }
    }
}

template<typename T>
void to_heap(std::vector<T>& arr)
{
  int num_elem = arr.size();
  int k = num_elem/2;
  while(k > 0)
  {
    sink<T>(arr, k, num_elem);
    k--;
  }
}

template<typename T>
void sort(std::vector<T>& arr){

  // create valid heap (in place)
  to_heap<T>(arr);

  int num_elem = arr.size();
  while(num_elem > 1)
  {
      std::swap(arr[0], arr[num_elem-1]);
      sink<T>(arr, 1, num_elem-1);
      num_elem--;
  }
}




}
