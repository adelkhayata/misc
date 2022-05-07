import ctypes

def compare_templates(template1, template2):
    if settings.Windows:
        dpfj_dll = ctypes.CDLL("dpfj.dll")  # Windows Lib
    else:
        dpfj_dll = ctypes.CDLL("libdpfj.so.3.1.0")  # Linux Lib
    dpfj_compare = dpfj_dll.dpfj_compare

    dpfj_compare.restype = ctypes.c_int

    dpfj_compare.argtypes = [
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
        ctypes.c_uint,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
        ctypes.c_uint,
        ctypes.POINTER(ctypes.c_uint),
    ]

    fmd1_type = 2
    fmd1 = template1
    fmd1_size = len(fmd1)
    fmd1_view_idx = 0
    fmd2_type = 1
    fmd2 = template2
    fmd2_size = len(fmd2)
    fmd2_view_idx = 0
    score = ctypes.c_uint(0)

    result = dpfj_compare(
        fmd1_type,
        fmd1,
        fmd1_size,
        fmd1_view_idx,
        fmd2_type,
        fmd2,
        fmd2_size,
        fmd2_view_idx,
        ctypes.byref(score),
    )

    accepted_score = 21474  # This comes by PROBABILITY_ONE / 100000 where PROBABILITY_ONE = 0x7fffffff

    if (int(score.value) < accepted_score) and (result == 0):
        return True
    else:
        return False
