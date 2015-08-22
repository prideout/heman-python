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
%rename (heman_export_u8) export_u8;
%rename (heman_lighting_apply) lighting_apply;

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

void export_u8(
    heman_image* source, HEMAN_FLOAT minv, HEMAN_FLOAT maxv,
    int DIM1, unsigned char* INPLACE_ARRAY1)
{
    heman_export_u8(source, minv, maxv, INPLACE_ARRAY1);
}

heman_image* lighting_apply(heman_image* heightmap,
    heman_image* colorbuffer, float occlusion, float diffuse,
    float diffuse_softening, float lx, float ly, float lz)
{
    float lightpos[3] = { lx, ly, lz };
    return heman_lighting_apply(heightmap,
        colorbuffer, occlusion, diffuse,
        diffuse_softening, lightpos);
}
%}
