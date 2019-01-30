#include <iostream>
#include <sys/ipc.h>
#include <sys/stat.h>
#include <typeinfo>

void printBits(size_t const size, void const * const ptr)
{
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;

    for (i=size-1;i>=0;i--)
    {
        for (j=7;j>=0;j--)
        {
            byte = (b[i] >> j) & 1;
            printf("%u", byte);
        }
    }
    puts("");
}

key_t ftok (const char *pathname, int proj_id){
  struct stat64 st;
  key_t key;

  if (__xstat64 (_STAT_VER, pathname, &st) < 0)
    return (key_t) -1;

  //The st_ino and st_dev, taken together, uniquely identify the file. The st_dev value is not necessarily consistent across reboots or system crashes, however.
  std::cout<< "st.st_ino: " << st.st_ino << " unique number of file " << std::endl;
  __ino64_t a = 0xffff;
  __ino64_t r1 = (st.st_ino & 0xffff);
  printBits(sizeof(a), &a);
  printBits(sizeof(st.st_ino ), &st.st_ino );
  printBits(sizeof(r1), &r1 );
  std::cout<< "r1: " << r1 << "\n" << std::endl;

  __ino64_t b = 0xff;
  __ino64_t r2 = (st.st_dev & 0xffff);
  printBits(sizeof(b), &b);
  printBits(sizeof(st.st_dev ), &st.st_dev );
  printBits(sizeof(r2), &r2 );
  std::cout<< "r2: " << r2 << std::endl;

  key = ((st.st_ino & 0xffff) | ((st.st_dev & 0xff) << 16) | ((proj_id & 0xff) << 24));

  return key;
}


int main(int argc, char *argv[])
{
    key_t key = ftok("/tmp", 1);
    std::cout<< "key: " << key << std::endl;
    return 0;
}
