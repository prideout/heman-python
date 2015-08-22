%module heman

%{
#define SWIG_FILE_WITH_INIT
#include "heman.h"
%}

%include "numpy.i"

%init %{
import_array();
%}

%include "../ext/include/heman.h"
