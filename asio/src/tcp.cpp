#include <iostream>
#include <boost/array.hpp>
#include <boost/asio.hpp>
using boost::asio::ip::tcp;

int main()
{
    std::string hostname = "localhost";
    boost::asio::io_service io_service;
    tcp::resolver resolver(io_service);


    tcp::resolver::query query(hostname, "13");

    tcp::resolver::iterator endpoint_iterator = resolver.resolve(query);
    tcp::socket socket(io_service);
    boost::asio::connect(socket, endpoint_iterator);

    try{
        for(;;){
            boost::array<char, 1> buf; // size of buffer does not seem to mater.
            boost::system::error_code error;
            // The boost::asio::buffer() function automatically determines the size of the array to help prevent buffer overruns.
            size_t len = socket.read_some(boost::asio::buffer(buf), error);
            if (error == boost::asio::error::eof){
                break; // Connection closed cleanly by peer.
            }else if (error){
                throw boost::system::system_error(error); // Some other error.
            }
            std::cout.write(buf.data(), len);
        }
    }catch(std::exception& e){
        std::cerr << e.what() << std::endl;
    }

  return 0;
}
