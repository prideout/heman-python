%module heman

%{
#define SWIG_FILE_WITH_INIT
#include "heman.h"
%}

heman_image* heman_image_create(int width, int height, int nbands);
void heman_image_destroy(heman_image*);
