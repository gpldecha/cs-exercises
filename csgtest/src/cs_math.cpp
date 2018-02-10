#include "cs_math.h"
#include <cmath>

double math::squareRoot(const double a) {
    double b = std::sqrt(a);
    if(b != b) { // nan check
        return -1.0;
    }else{
        return sqrt(a);
    }
}
