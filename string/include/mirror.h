#ifndef MIRROR_H_
#define MIRROR_H_

#include <string>
#include <functional>
#include <iostream>

class Mirror{

	public:


    static std::string vertMirror(const std::string &input){

          // treat each line independently
          // find number of lines
          std::size_t n = input.find('\n');
          std::string output("");

         if(n != std::string::npos){

           int start = 0;
           int end = n;
           std::string substr;

           for(int i = 0; i < n;i++)
           {

             std::cout<< "s: " << start <<  " " << input[start] << std::endl;

             substr = input.substr(start,n);
             std::cout<< substr << std::endl;
             for(int j = substr.size()-1; j >= 0;j--)
             {
               output.push_back(substr[j]);
             }

             if(i != n-1){
                output.append("\n");
                start = end + 1;
                end   = start + n;
             }


           }



          }


          return output;
        }

          static std::string horMirror(const std::string &input){
              std::string output("");
              std::size_t n = input.find('\n');
              int start = input.size()-n;
              std::string substr;
              for(int i = 0; i < n;i++)
              {
                  substr = input.substr(start,n);
                  output.append(substr);
                  start = start - n -1;

                  if(i != n-1)
                  {
                      output.append("\n");
                  }

              }
          return output;
        }

        // your high order function oper
        //... oper(...);
        static std::string oper( std::function<std::string(const std::string&)> fct, const std::string &s){
          return fct(s);
        }


};


void vitrical_test()
{
    std::string s = "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu";
    std::string sol = "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw";

    std::string output = Mirror::vertMirror(s);

    std::cout<< "Lenghts: " << output.size() << " " << sol.size() << std::endl;
    for(std::size_t i = 0; i < sol.size();i++)
    {
        if(output[i] != sol[i])
        {
            std::cout<< "i: " << i << std::endl;
        }
    }

    if(output == sol)
    {
        std::cout<< "Correct" << std::endl;
    }else{
        std::cout<< "Not correct" << std::endl;
    }
    std::cout<< "\n\n\n" << std::endl;
    std::cout<< output << std::endl;
    std::cout<< "\n\n\n" << std::endl;
    std::cout<< sol << std::endl;

}

#endif
