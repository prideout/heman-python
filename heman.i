%module heman

%{
#define SWIG_FILE_WITH_INIT
#include "heman.h"
%}

%include "numpy.i"

%init %{
import_array();
%}

heman_image* heman_image_create(int width, int height, int nbands);
void heman_image_destroy(heman_image*);
heman_image* heman_generate_island_heightmap(int width, int height, int seed);
void heman_image_array(heman_image* img, float** ARGOUTVIEW_ARRAY1, int* DIM1);
