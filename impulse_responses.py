import numpy as np

def rayleighSommerfeld(x_grid,y_grid,z,wavelength=None):
    if wavelength == None:
        wavelength = physops.DEFAULT_WAVELENGTH

    amp = 1.0 / np.sqrt(x_grid**2 + y_grid**2 + z**2)
    phase = (2*np.pi*np.sqrt(x_grid**2 + y_grid**2 + z**2) / wavelength).astype(np.complex128)
    impulse_response = amp * np.exp(1j * phase)
    return impulse_response


def fresnel(x_grid,y_grid,z,wavelength=None):
    if wavelength == None:
        wavelength = physops.DEFAULT_WAVELENGTH

    amp = 1.0 / z
    phaseZ = (2*np.pi*(z/wavelength)).astype(np.complex128)
    phaseXY = (np.pi*(x_grid**2 + y_grid**2)/(wavelength * z)).astype(np.complex128)
    impulse_response = amp * np.exp(1j * phaseZ) * np.exp(1j * phaseXY)
    return impulse_response
