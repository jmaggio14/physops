import numpy as np
import copy


def magnitude(wavefront):
    wavefront_copy = copy.deepcopy(wavefront)
    wavefront_copy.imag = wavefront_copy.imag * -1
    magnitude = wavefront * wavefront_copy

    return magnitude


def phase(wavefront):
    phase = np.arctan( wavefront.imag / wavefront.real )
    return phase
