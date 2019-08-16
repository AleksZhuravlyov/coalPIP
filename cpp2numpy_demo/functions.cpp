#include <functions.h>

np::ndarray returnArray() {

    int N = 10;
    p::tuple shape = p::make_tuple(N);
    np::dtype dtype = np::dtype::get_builtin<double>();
    np::ndarray array = np::zeros(shape, dtype);
    for (int i = 0; i < N; i++)
        array[i] = i;

    return array;
}

void squareArray(np::ndarray &array) {

    auto nd = array.get_nd();
    auto shape = array.get_shape();

    for (int i = 0; i < shape[nd - 1]; i++)
        array[i] = array[i] * array[i];

}

double sumArray(np::ndarray &array) {

    auto nd = array.get_nd();
    auto shape = array.get_shape();

    double sum = 0;
    for (int i = 0; i < shape[nd - 1]; i++)
        sum += p::extract<double>(array[i]);

    return sum;

}