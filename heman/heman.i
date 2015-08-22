%module heman

%{
#define SWIG_FILE_WITH_INIT
#include "heman.h"
%}

%include "numpy.i"
%include "typemaps.i"

%init %{
import_array();
%}

%apply int *OUTPUT { int* width, int* height, int* nbands };
%apply (float** ARGOUTVIEW_ARRAY1, int* DIM1) {(float** outview, int* n)};

%apply (int DIM1, int* IN_ARRAY1) {(int nlocs, int* locs)}
%apply (int DIM1, unsigned int* IN_ARRAY1) {(int ncols, unsigned int* cols)}

%include "../ext/include/heman.h"

%rename (heman_color_create_gradient) color_create_gradient;

%inline %{
heman_image* color_create_gradient(int width,
    int nlocs, int* locs, int ncols, unsigned int* cols)
{
    if (nlocs != ncols) {
        PyErr_Format(PyExc_ValueError,
                     "Arrays of lengths (%d,%d) given",
                     nlocs, nlocs);
        return 0;
    }
    return heman_color_create_gradient(width, ncols, locs, cols);
}
%}