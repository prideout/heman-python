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

%include "../ext/include/heman.h"
