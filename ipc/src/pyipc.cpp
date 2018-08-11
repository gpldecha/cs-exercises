#include <boost/python.hpp>
#include <boost/interprocess/xsi_shared_memory.hpp>
#include <boost/interprocess/mapped_region.hpp>
#include <iostream>

using namespace boost::interprocess;

#ifndef _XSI_H
#define _XSI_H

class Xsi{

public:

    void remove_old_shared_memory(const xsi_key &key){
        try{
            xsi_shared_memory xsi(open_only, key);
            xsi_shared_memory::remove(xsi.get_shmid());
        }
        catch(interprocess_exception &e){
            if(e.get_error_code() != not_found_error)
                throw;
        }
    }

public:

    Xsi(){

        char *path = "/tmp";

        //Build XSI key (ftok based)
        xsi_key key(path, 1);

        remove_old_shared_memory(key);

        //Create a shared memory object.
        shm = new xsi_shared_memory(create_only, key, 1);

        //Map the whole shared memory in this process
        region = new mapped_region(*shm, read_write);

    }

    ~Xsi(){
        //Remove shared memory on destruction
        struct shm_remove
        {
            int shmid_;
            shm_remove(int shmid) : shmid_(shmid){}
            ~shm_remove(){ xsi_shared_memory::remove(shmid_); }
        } remover(shm->get_shmid());
    }

    void ping(){
        std::memset(region->get_address(), i, region->get_size());
        i=(i+1)%128;
    }

private:

    xsi_shared_memory* shm;
    mapped_region* region;
    int i = 0;
};

#endif // _XSI_H


BOOST_PYTHON_MODULE(pyipc)
{
    using namespace boost::python;
    class_<Xsi>("Xsi")
     .def("ping", &Xsi::ping)
    ;
}
