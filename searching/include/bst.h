#ifndef BST_H_
#define BST_H_

#include <cstddef>
#include <iostream>

namespace bst{

class Node;

class Node{
public:
  Node(int key, int value, int count, Node* parent=NULL)
  :key(key), value(value), count(count), parent(parent){
    left = NULL;
    right = NULL;
  }
  int key, value, count;
  Node* left;
  Node* right;
  Node* parent;
};


int size(Node* node){
  if(node == NULL){return 0;}
  return node->count;
}

void print(Node* node){
  if (node == NULL) return;
  print(node->left);
  if(node->parent != NULL){
    std::cout<< node->key <<  "  count: " << node->count << " parent: " << node->parent->key << std::endl;
  }else{
    std::cout<< node->key <<  "  count: " << node->count << std::endl;
  }
  print(node->right);
}

Node* recursive_put(int key, int value, Node* node){
      if(node == NULL){
        return new Node(key, value, 1);
      }
      if(key < node->key){
        node->left = recursive_put(key, value, node->left);
      }else if(key > node->key){
        node->right = recursive_put(key, value, node->right);
      }else{  // key == node->key
        node->value = value;
      }
      node->count = 1 + size(node->left) + size(node->right);
      return node;
}

void put(int key, int value, Node* root){
        // find leaf node
        Node* current = root;
        Node* parent = NULL;
        while(current != NULL){
          parent = current;
          if(key < current->key){
            current = current->left;
          }else if(key > current->key){
            current = current->right;
          }else{
            current->value = value;
            return;
          }
        }
        current = parent;
        if(key < current->key){
          current->left = new Node(key, value, 1, current);
        }else{
          current->right = new Node(key, value, 1, current);
        }
        while(current != NULL){
          current->count++;
          current = current->parent;
        }
}

Node* get(int key, Node* node){
  if(node == NULL || node->key == key)
    return node;
  if(key < node->key){
    return get(key, node->left);
  }else{
    return get(key, node->right);
  }
}

Node* floor(int k, Node* node){
    if(node == NULL)
      return node;
    if(node->key == k)
      return node;
    if(k < node->key)
      return floor(k, node->left);

    Node* t = floor(k, node->right);
    if(t != NULL){
      return t;
    }else{
      return node;
    }
}

int rank(int key, Node* node){
  if(node == NULL){
    return 0;
  }
  if(node->key == key){
    return size(node->left);
  }else if(key < node->key){
    return rank(key, node->left);
  }else{
    return 1 + size(node->left) + rank(key, node->right);
  }
}

void decrement_cound(Node* node){
  while(node != NULL){
    node->count--;
    node = node->parent;
  }
}

Node* min_node(Node* node){
  if(node->left == NULL)
    return node;
  while(node->left != NULL){
    node = node->left;
  }
  return node;
}

void deleteMin(Node* node){
  while(node->left != NULL)
    node = node->left;

  node->parent->left = node->right;
  Node *current = node->parent;
  delete node;
  decrement_cound(current);
}

 Node* delete_min_recursive(Node* node)
{
  if(node->left == NULL){
    Node* right = node->right;
    delete node;
    return right;
  }
  node->left = delete_min_recursive(node->left);
  node->count = 1 + bst::size(node->left) + bst::size(node->right);
  return node;
}

Node* delete_recursive(int key, Node* node){
  if(node == NULL){
    return node;
  }
  if(key < node->key){
    node->left = delete_recursive(key, node->left);
  }else if(key > node->key){
    node->right = delete_recursive(key, node->right);
  }else{
    if(node->right == NULL)
        return node->left;
    if(node->left == NULL);
        return node->right;

    Node* t = node;
    //Node* sucessor = bst::min_node(t.right);
  }
}

void delete_iterative(int key, Node* node){
  Node* t = bst::get(key, node);
  if(t == NULL)
    return;

  Node **branch;
  if(t->parent->left == t){
    branch = &(t->parent->left);
  }else{
    branch = &(t->parent->right);
  }

  if(t->count == 1){
    *branch = NULL;
    decrement_cound(t->parent);
  }else if(t->count == 2){
    if(t->left != NULL){
      *branch = t->left;
    }else{
      *branch = t->right;
    }
    decrement_cound(t->parent);
  }else{
    Node* successor = min_node(t->right);
    Node* successor_parent = successor->parent;
    // remove sucessor and update parents left child.

    if(successor->right != NULL){
      successor_parent->left = successor->right;
    }else{
      successor_parent->left = NULL;
    }
    // replace sucessor with t
    *branch = successor;
    successor->count = t->count;
    successor->parent = t->parent;
    successor->left = t->left;
    successor->right = t->right;

    t->left->parent = successor;
    t->right->parent = successor;

    decrement_cound(successor_parent);
  }
  delete t;


}



class BinarySearchTree{

  public:

    Node* root;

  public:

    BinarySearchTree(){
      root = NULL;
    }

    void insert(int key, int value){
      if(root == NULL){
        root = new Node(key, value, 1);
      }else{
        put(key, value, root);
      }
    }

    void delete_key(int key){
      bst::delete_iterative(key, root);
    }

    Node* get(int key){
      return bst::get(key, root);
    }

    int size(){
      return bst::size(root);
    }

    void print(){
      bst::print(root);
    }

    void delete_min(){
      bst::deleteMin(root);
    }

    int min(){
      if(root->left == NULL)
        return root->key;
      Node* node = root;
      while(node->left != NULL){
        node = node->left;
      }
      return node->key;
    }

    int max(){
      if(root->right == NULL)
        return root->key;
      Node* node = root;
      while(node->right != NULL){
        node = node->right;
      }
      return node->key;
    }

    int floor(int key){
      Node* node = bst::floor(key, root);
      if(node == NULL){
        return -1;
      }else{
        return node->key;
      }
    }

};

}


#endif
