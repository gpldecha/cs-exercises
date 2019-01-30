#include <boost/interprocess/xsi_shared_memory.hpp>
#include <boost/interprocess/mapped_region.hpp>
#include <cstring>
#include <cstdlib>
#include <string>
#include <iostream>
#include <chrono>
#include <thread>
using namespace boost::interprocess;

// https://fscked.org/writings/SHM/shm-5.html

void remove_old_shared_memory(const xsi_key &key)
{
    try{
        xsi_shared_memory xsi(open_only, key);
        xsi_shared_memory::remove(xsi.get_shmid());
    }
    catch(interprocess_exception &e){
        if(e.get_error_code() != not_found_error)
            throw;
    }
}

int main(int argc, char *argv[])
{

    char *path = "/tmp";

    //Build XSI key (ftok based)
    xsi_key key(path, 1);

    std::cout<< "KEY: " << key.get_key() << std::endl;

    remove_old_shared_memory(key);

    //Create a shared memory object.
    xsi_shared_memory shm(create_only, key, 1);

    //Remove shared memory on destruction
    struct shm_remove
    {
        int shmid_;
        shm_remove(int shmid) : shmid_(shmid){}
        ~shm_remove(){ xsi_shared_memory::remove(shmid_); }
    } remover(shm.get_shmid());

    //Map the whole shared memory in this process
    mapped_region region(shm, read_write);

    int i = 1;
    while(true){
        std::memset(region.get_address(), i, region.get_size());
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
        i=(i+1)%128;
    }
    return 0;
}
