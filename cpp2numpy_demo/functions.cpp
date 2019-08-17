#include <functions.h>

np::ndarray returnArray() {

    int N = 10;
    p::tuple shape = p::make_tuple(N);
    np::dtype dtype = np::dtype::get_builtin<double>();
    np::ndarray array = np::zeros(shape, dtype);
    auto arrayPtr = (double *) array.get_data();
    for (int i = 0; i < N; i++)
        arrayPtr[i] = i;

    return array;
}

void squareArray(np::ndarray &array) {

    auto nd = array.get_nd();
    auto shape = array.get_shape();
    auto arrayPtr = (double *) array.get_data();
    for (int i = 0; i < shape[nd - 1]; i++)
        arrayPtr[i] = arrayPtr[i] * arrayPtr[i];

}

double sumArray(np::ndarray &array) {

    auto shape = array.get_shape();
    auto arrayPtr = (double *) array.get_data();
    double arraySum = 0;
    for (int i = 0; i < shape[0]; i++)
        arraySum += arrayPtr[i];

    return arraySum;

}