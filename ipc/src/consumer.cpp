#include <boost/interprocess/xsi_shared_memory.hpp>
#include <boost/interprocess/mapped_region.hpp>
#include <cstring>
#include <cstdlib>
#include <string>
#include <iostream>
#include <chrono>
#include <thread>

using namespace boost::interprocess;


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

    //Create a shared memory object.
    xsi_shared_memory shm (open_only, key);

    //Map the whole shared memory in this process
    mapped_region region(shm, read_only);

    //Check that memory was initialized to 1
    char *mem = static_cast<char*>(region.get_address());

    while(true){
        for(std::size_t i = 0; i < region.get_size(); ++i){
            std::cout<< (int)mem[i] << std::endl;
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
    return 0;
}
