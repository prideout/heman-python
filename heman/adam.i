%module adam

%{
#define SWIG_FILE_WITH_INIT
#include "heman.h"
%}

%inline %{
    typedef heman_image* heman_image_ptr;
%}

%include "numpy.i"
%include "typemaps.i"
%include "carrays.i"

%init %{
import_array();
%}

%apply int *OUTPUT { int* width, int* height, int* nbands };
%apply (float** ARGOUTVIEW_ARRAY1, int* DIM1) {(float** outview, int* n)};
%apply (int DIM1, int* IN_ARRAY1) {(int nlocs, int* locs)}
%apply (int DIM1, unsigned int* IN_ARRAY1) {(int ncols, unsigned int* cols)}

%array_class(heman_image_ptr, HemanImageArray);

%include "../ext/include/heman.h"

%rename (heman_points_create) points_create;
%rename (heman_color_create_gradient) color_create_gradient;
%rename (heman_export_u8) export_u8;
%rename (heman_import_u8) import_u8;
%rename (heman_lighting_apply) lighting_apply;

%inline %{
heman_points* points_create(int DIM1, float* IN_ARRAY1, int nbands)
{
    return heman_points_create(IN_ARRAY1, DIM1 / nbands, nbands);
}

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

heman_image* import_u8(int width, int height, int nbands,
    int DIM1, unsigned char* IN_ARRAY1, HEMAN_FLOAT minval, HEMAN_FLOAT maxval)
{
    return heman_import_u8(width, height, nbands, IN_ARRAY1, minval, maxval);
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
