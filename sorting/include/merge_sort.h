#ifndef MERGE_SORT_H_
#define MERGE_SORT_H_

#include <cstring>



template<typename T>
class merge_sort{

private:

    /**
    * @brief merge
    * @param a_ptr     : pointer to array a
    * @param aux_ptr   : pointer to auxilary array
    * @param lo        : lower index
    * @param mid       : middle index
    * @param hi        : higher index
    */
    void static merge(T* a_ptr, T* aux_ptr, std::size_t num_elem, std::size_t lo, std::size_t mid, std::size_t hi, bool (*comp)(T,T))
    {
        // a_ptr[lo    ... mid] is sorted
        // a_ptr[mid+1 ... hi] is sorted

        // copy a_ptr into aux_ptr
        std::memcpy(aux_ptr,a_ptr,num_elem * sizeof(T));

        std::size_t i = lo;
        std::size_t j = mid+1;
        for(std::size_t k = lo; k <= hi;k++)
        {
            if(i > mid){                            // if first sub array has filled target
                a_ptr[k] = aux_ptr[j]; j++;
            }else if (j > hi)                       // if second sub array has filled target
            {
                a_ptr[k] = aux_ptr[i]; i++;
            }else if(comp(aux_ptr[i],aux_ptr[j]))   // if aux_ptr[i] is greater/less than aux_ptr[j]
            {
                a_ptr[k] = aux_ptr[i]; i++;
            }else{
                a_ptr[k] = aux_ptr[j]; j++;
            }
        }
    }


private:

    void static sort(T *a_ptr, T* aux_ptr, std::size_t num_elem,std::size_t lo, std::size_t hi, bool (*comp)(T, T)){

         if(lo == hi)
             return;
         assert(lo < hi);
         std::size_t mid = lo + (hi - lo) / 2;

         sort(a_ptr,aux_ptr,num_elem,lo,mid,comp);           // recursive call
         sort(a_ptr,aux_ptr,num_elem,mid+1,hi,comp);

         merge(a_ptr,aux_ptr,num_elem,lo,mid,hi,comp);
    }


public:

    void static sort(T* a_ptr,std::size_t num_elem, bool (*comp)(T,T))
    {
        assert(num_elem >= 2);
        // create auxiliary array
        T* aux_ptr = new T[num_elem];


        sort(a_ptr,aux_ptr,num_elem,0,num_elem-1,comp);


        delete[] aux_ptr;
    }




};





#endif
