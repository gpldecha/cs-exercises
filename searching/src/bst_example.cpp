#include "bst.h"


void example1(){
  std::cout<< "bst example" << std::endl;

  using namespace bst;

  BinarySearchTree bst;

  bst.insert(20, 0);
  bst.insert(15, 0);
  bst.insert(25, 0);
  bst.insert(12, 0);
  bst.insert(18, 0);
  bst.insert(22, 0);
  bst.insert(28, 0);
  // bst.insert(11, 0);

  print(bst.root);

  std::cout<< " delete  " << std::endl;
  bst.delete_min();

  print(bst.root);

  int k = 25;
  Node* result = bst.get(k);
  if(result != NULL){
    std::cout<< "found node with key: " << result->key << std::endl;
  }else{
    std::cout<< "did not find node with key: " << k << std::endl;
  }
  std::cout<< "min: " << bst.min() << std::endl;
  std::cout<< "max: " << bst.max() << std::endl;

  k = 13;
  std::cout<< "foor("<< k << "): " << bst.floor(k) << std::endl;

}

void example2(){
  std::cout<< "bst example 2" << std::endl;

  using namespace bst;

  BinarySearchTree bst;

  bst.insert(30, 0);
  bst.insert(15, 0);
  bst.insert(14, 0);
  bst.insert(20, 0);
  bst.insert(17, 0);
  bst.insert(25, 0);
  bst.insert(16, 0);
  bst.insert(18, 0);

  print(bst.root);

  int key_delete = 15;
  std::cout<< "delete key: " <<  key_delete << std::endl;
  bst.delete_key(key_delete);
  print(bst.root);

}


int main(int argc, char** argv)
{
  example2();
  return 0;
}
