# python build stubs for package dither_go
# File is generated by gopy. Do not edit.
# gopy build -no-make -output=dither_go/bindings -vm=python3 ./dither_go github.com/tfuxu/dither-gopy

from pybindgen import retval, param, Function, Module
import sys

class CheckedFunction(Function):
    def __init__(self, *a, **kw):
        super(CheckedFunction, self).__init__(*a, **kw)
        self._failure_expression = kw.get('failure_expression', '')
        self._failure_cleanup = kw.get('failure_cleanup', '')

    def set_failure_expression(self, expr):
        self._failure_expression = expr

    def set_failure_cleanup(self, expr):
        self._failure_cleanup = expr

    def generate_call(self):
        super(CheckedFunction, self).generate_call()
        check = "PyErr_Occurred()"
        if self._failure_expression:
            check = "{} && {}".format(self._failure_expression, check)
        failure_cleanup = self._failure_cleanup or None
        self.before_call.write_error_check(check, failure_cleanup)

def add_checked_function(mod, name, retval, params, failure_expression='', *a, **kw):
    fn = CheckedFunction(name, retval, params, *a, **kw)
    fn.set_failure_expression(failure_expression)
    mod._add_function_obj(fn)
    return fn

def add_checked_string_function(mod, name, retval, params, failure_expression='', *a, **kw):
    fn = CheckedFunction(name, retval, params, *a, **kw)
    fn.set_failure_cleanup('if (retval != NULL) free(retval);')
    fn.after_call.add_cleanup_code('free(retval);')
    fn.set_failure_expression(failure_expression)
    mod._add_function_obj(fn)
    return fn

mod = Module('_dither_go')
mod.add_include('"dither_go_go.h"')
mod.add_function('GoPyInit', None, [])
mod.add_function('DecRef', None, [param('int64_t', 'handle')])
mod.add_function('IncRef', None, [param('int64_t', 'handle')])
mod.add_function('NumHandles', retval('int'), [])
mod.add_function('color_Palette_CTor', retval('int64_t'), [])
mod.add_function('color_Palette_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('color_Palette_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('color_Palette_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('color_Palette_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('color_Palette_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_bool_CTor', retval('int64_t'), [])
mod.add_function('Slice_bool_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_bool_elem', retval('bool'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_bool_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_bool_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('bool', 'value')])
mod.add_function('Slice_bool_append', None, [param('int64_t', 'handle'), param('bool', 'value')])
mod.add_function('Slice_byte_CTor', retval('int64_t'), [])
mod.add_function('Slice_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_byte_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_byte_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_byte_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_error_CTor', retval('int64_t'), [])
mod.add_function('Slice_error_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_error_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_error_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_error_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_error_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_float32_CTor', retval('int64_t'), [])
mod.add_function('Slice_float32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float32_elem', retval('float'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_float32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('float', 'value')])
mod.add_function('Slice_float32_append', None, [param('int64_t', 'handle'), param('float', 'value')])
mod.add_function('Slice_float64_CTor', retval('int64_t'), [])
mod.add_function('Slice_float64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float64_elem', retval('double'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_float64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('double', 'value')])
mod.add_function('Slice_float64_append', None, [param('int64_t', 'handle'), param('double', 'value')])
mod.add_function('Slice_int_CTor', retval('int64_t'), [])
mod.add_function('Slice_int_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int16_CTor', retval('int64_t'), [])
mod.add_function('Slice_int16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int16_elem', retval('int16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int16_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int16_t', 'value')])
mod.add_function('Slice_int16_append', None, [param('int64_t', 'handle'), param('int16_t', 'value')])
mod.add_function('Slice_int32_CTor', retval('int64_t'), [])
mod.add_function('Slice_int32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int32_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_int32_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_int64_CTor', retval('int64_t'), [])
mod.add_function('Slice_int64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int64_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int64_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int8_CTor', retval('int64_t'), [])
mod.add_function('Slice_int8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int8_elem', retval('int8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int8_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int8_t', 'value')])
mod.add_function('Slice_int8_append', None, [param('int64_t', 'handle'), param('int8_t', 'value')])
mod.add_function('Slice_rune_CTor', retval('int64_t'), [])
mod.add_function('Slice_rune_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_rune_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_rune_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_rune_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_rune_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_string_CTor', retval('int64_t'), [])
mod.add_function('Slice_string_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_string_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_string_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_string_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_string_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_uint_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint16_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint16_elem', retval('uint16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint16_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint16_t', 'value')])
mod.add_function('Slice_uint16_append', None, [param('int64_t', 'handle'), param('uint16_t', 'value')])
mod.add_function('Slice_uint32_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint32_elem', retval('uint32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint32_t', 'value')])
mod.add_function('Slice_uint32_append', None, [param('int64_t', 'handle'), param('uint32_t', 'value')])
mod.add_function('Slice_uint64_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint64_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint64_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint8_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint8_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint8_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_uint8_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_color_Color_CTor', retval('int64_t'), [])
mod.add_function('Slice_color_Color_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_color_Color_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_color_Color_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_color_Color_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_color_Color_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
add_checked_function(mod, 'dither_go_CreatePalette', retval('int64_t'), [param('int64_t', 'colors')])
add_checked_function(mod, 'dither_go_CreateRGBA', retval('int64_t'), [param('uint8_t', 'r'), param('uint8_t', 'g'), param('uint8_t', 'b'), param('uint8_t', 'a')])
add_checked_function(mod, 'dither_go_OpenImage', retval('int64_t'), [param('char*', 'path')])
add_checked_function(mod, 'dither_go_SaveImage', retval('char*'), [param('int64_t', 'img_data'), param('char*', 'output_path'), param('char*', 'encode_format')])
mod.add_function('Slice_Slice_uint_CTor', retval('int64_t'), [])
mod.add_function('Slice_Slice_uint_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Slice_uint_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Slice_uint_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_Slice_uint_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Slice_uint_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('dither_Atkinson', retval('int64_t'), [])
mod.add_function('dither_Set_Atkinson', None, [param('int64_t', 'val')])
mod.add_function('dither_Burkes', retval('int64_t'), [])
mod.add_function('dither_Set_Burkes', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDot4x4', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDot4x4', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDot6x6', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDot6x6', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDot6x6_2', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDot6x6_2', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDot6x6_3', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDot6x6_3', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDot8x8', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDot8x8', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDotDiagonal16x16', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDotDiagonal16x16', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDotDiagonal6x6', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDotDiagonal6x6', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDotDiagonal8x8', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDotDiagonal8x8', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDotDiagonal8x8_2', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDotDiagonal8x8_2', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDotDiagonal8x8_3', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDotDiagonal8x8_3', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDotHorizontalLine', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDotHorizontalLine', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDotSpiral5x5', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDotSpiral5x5', None, [param('int64_t', 'val')])
mod.add_function('dither_ClusteredDotVerticalLine', retval('int64_t'), [])
mod.add_function('dither_Set_ClusteredDotVerticalLine', None, [param('int64_t', 'val')])
mod.add_function('dither_FalseFloydSteinberg', retval('int64_t'), [])
mod.add_function('dither_Set_FalseFloydSteinberg', None, [param('int64_t', 'val')])
mod.add_function('dither_FloydSteinberg', retval('int64_t'), [])
mod.add_function('dither_Set_FloydSteinberg', None, [param('int64_t', 'val')])
mod.add_function('dither_Horizontal3x5', retval('int64_t'), [])
mod.add_function('dither_Set_Horizontal3x5', None, [param('int64_t', 'val')])
mod.add_function('dither_JarvisJudiceNinke', retval('int64_t'), [])
mod.add_function('dither_Set_JarvisJudiceNinke', None, [param('int64_t', 'val')])
mod.add_function('dither_Sierra', retval('int64_t'), [])
mod.add_function('dither_Set_Sierra', None, [param('int64_t', 'val')])
mod.add_function('dither_Sierra2', retval('int64_t'), [])
mod.add_function('dither_Set_Sierra2', None, [param('int64_t', 'val')])
mod.add_function('dither_Sierra2_4A', retval('int64_t'), [])
mod.add_function('dither_Set_Sierra2_4A', None, [param('int64_t', 'val')])
mod.add_function('dither_Sierra3', retval('int64_t'), [])
mod.add_function('dither_Set_Sierra3', None, [param('int64_t', 'val')])
mod.add_function('dither_SierraLite', retval('int64_t'), [])
mod.add_function('dither_Set_SierraLite', None, [param('int64_t', 'val')])
mod.add_function('dither_Simple2D', retval('int64_t'), [])
mod.add_function('dither_Set_Simple2D', None, [param('int64_t', 'val')])
mod.add_function('dither_StevenPigeon', retval('int64_t'), [])
mod.add_function('dither_Set_StevenPigeon', None, [param('int64_t', 'val')])
mod.add_function('dither_Stucki', retval('int64_t'), [])
mod.add_function('dither_Set_Stucki', None, [param('int64_t', 'val')])
mod.add_function('dither_TwoRowSierra', retval('int64_t'), [])
mod.add_function('dither_Set_TwoRowSierra', None, [param('int64_t', 'val')])
mod.add_function('dither_Vertical5x3', retval('int64_t'), [])
mod.add_function('dither_Set_Vertical5x3', None, [param('int64_t', 'val')])
mod.add_function('dither_Ditherer_CTor', retval('int64_t'), [])
mod.add_function('dither_Ditherer_Matrix_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('dither_Ditherer_Matrix_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('dither_Ditherer_Special_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('dither_Ditherer_Special_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('dither_Ditherer_SingleThreaded_Get', retval('bool'), [param('int64_t', 'handle')])
mod.add_function('dither_Ditherer_SingleThreaded_Set', None, [param('int64_t', 'handle'), param('bool', 'val')])
mod.add_function('dither_Ditherer_Serpentine_Get', retval('bool'), [param('int64_t', 'handle')])
mod.add_function('dither_Ditherer_Serpentine_Set', None, [param('int64_t', 'handle'), param('bool', 'val')])
add_checked_function(mod, 'dither_Ditherer_SetBayer', None, [param('int64_t', '_handle'), param('uint64_t', 'x'), param('uint64_t', 'y'), param('float', 'strength'), param('bool', 'goRun')])
add_checked_function(mod, 'dither_Ditherer_SetOrdered', None, [param('int64_t', '_handle'), param('int64_t', 'odm'), param('float', 'strength'), param('bool', 'goRun')])
add_checked_function(mod, 'dither_Ditherer_SetRandomGrayscale', None, [param('int64_t', '_handle'), param('float', 'min'), param('float', 'max'), param('bool', 'goRun')])
add_checked_function(mod, 'dither_Ditherer_SetRandomRGB', None, [param('int64_t', '_handle'), param('float', 'minR'), param('float', 'maxR'), param('float', 'minG'), param('float', 'maxG'), param('float', 'minB'), param('float', 'maxB'), param('bool', 'goRun')])
add_checked_function(mod, 'dither_Ditherer_ClearMapper', None, [param('int64_t', '_handle'), param('bool', 'goRun')])
add_checked_function(mod, 'dither_Ditherer_GetPalette', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'dither_Ditherer_Dither', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'src')])
add_checked_function(mod, 'dither_Ditherer_GetColorModel', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'dither_Ditherer_DitherCopy', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'src')])
add_checked_function(mod, 'dither_Ditherer_DitherPaletted', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'src')])
add_checked_function(mod, 'dither_Ditherer_Draw', None, [param('int64_t', '_handle'), param('int64_t', 'dst'), param('int64_t', 'r'), param('int64_t', 'src'), param('int64_t', 'sp'), param('bool', 'goRun')])
add_checked_function(mod, 'dither_Ditherer_Quantize', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'p'), param('int64_t', 'm')])
mod.add_function('dither_OrderedDitherMatrix_CTor', retval('int64_t'), [])
mod.add_function('dither_OrderedDitherMatrix_Matrix_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('dither_OrderedDitherMatrix_Matrix_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('dither_OrderedDitherMatrix_Max_Get', retval('uint64_t'), [param('int64_t', 'handle')])
mod.add_function('dither_OrderedDitherMatrix_Max_Set', None, [param('int64_t', 'handle'), param('uint64_t', 'val')])
mod.add_function('dither_ErrorDiffusionMatrix_CTor', retval('int64_t'), [])
mod.add_function('dither_ErrorDiffusionMatrix_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('dither_ErrorDiffusionMatrix_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('dither_ErrorDiffusionMatrix_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('dither_ErrorDiffusionMatrix_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('dither_ErrorDiffusionMatrix_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
add_checked_function(mod, 'dither_ErrorDiffusionMatrix_CurrentPixel', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'dither_NewDitherer', retval('int64_t'), [param('int64_t', 'palette')])
add_checked_function(mod, 'dither_ErrorDiffusionStrength', retval('int64_t'), [param('int64_t', 'edm'), param('float', 'strength')])
add_checked_function(mod, 'dither_RoundClamp', retval('uint16_t'), [param('float', 'i')])

mod.generate(open('dither_go.c', 'w'))

