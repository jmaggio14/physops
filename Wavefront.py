import numpy as np
import physops
import scipy

class Wavefront(np.ndarray):
    def __new__(cls,definition=None,title="wavefront",wavelength=None,size=(1000,1000),x_range=None,y_range=None,definition_kwargs={}):
        if x_range == None:
            x_range = np.linspace(-size[0]//2,size[0]//2,size[0])
        if y_range == None:
            y_range = np.linspace(-size[1]//2,size[1]//2,size[1])
        if wavelength == None:
            wavelength = physops.DEFAULT_WAVELENGTH

        x_grid,y_grid = np.meshgrid(x_range,y_range)

        wavefront = np.asarray(definition(x_grid,y_grid,**definition_kwargs),np.complex128)

        obj = np.asarray(wavefront).view(cls)
        obj.x_grid = x_grid
        obj.y_grid = y_grid
        obj.wavelength = wavelength
        obj.definition = definition
        obj.definition_kwargs = definition_kwargs
        obj.title = title

        return obj


    def __array_finalize__(self,obj):
        if obj is None:
            return None
        self.x_grid = getattr(obj,"x_grid",None)
        self.y_grid = getattr(obj,"y_grid",None)
        self.wavelength = getattr(obj,"wavelength",None)
        self.definition = getattr(obj,"definition",None)
        self.definition_kwargs = getattr(obj,"definition_kwargs",None)
        self.title = getattr(obj,"title",None)

    def __array_wrap__(self,out_arr,context=None):
        return np.ndarray.__array_wrap__(self,out_arr,context)


    def __gt__(self,z):
        """
        overloaded operator to propagate an operation with rayleigh-sommerfeld
        impulse response
        """
        if isinstance(z,(int,float)):
            impulse_response = physops.rayleighSommerfeld(x_grid=self.x_grid,y_grid=self.y_grid,z=z,wavelength=self.wavelength)
            new_wavefront = scipy.signal.convolve2d(self,impulse_response,mode="same")
            new_wavefront.title += ">{0}".format(z)
            return new_wavefront

    def __rrshift__(self,z):
        if isinstance(z,(int,float)):
            impulse_response = physops.fresnel(x_grid=x_grid,y_grid=y_grid,z=z,wavelength=self.wavelength)
            new_wavefront = scipy.signal.convolve2d(self,impulse_response,mode="same")
            new_wavefront.title += ">>{0}".format(z)
            return new_wavefront


    # def __or__(self,z):
    #
