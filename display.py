import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import physops


def display(src,title=None):
    if isinstance(src,physops.Wavefront):
        fig = plt.figure(edgecolor="white")

        plt.title(src.title if isinstance(title,type(None)) else str(title))

        img = src.real.astype(np.float64)
        ax = fig.add_subplot(221)
        ax.title.set_text("REAL")
        # ax.title.set_color(color="white")
        plot = plt.imshow(img,cmap="gray",extent=[src.x_grid.min(),src.x_grid.max(),src.y_grid.min(),src.y_grid.max()])
        plt.colorbar(plot,ax=ax)

        img = src.imag.astype(np.float64)
        ax = fig.add_subplot(222)
        ax.title.set_text("IMAG")
        # ax.title.set_color(color="white")
        plot = plt.imshow(img,cmap="gray",extent=[src.x_grid.min(),src.x_grid.max(),src.y_grid.min(),src.y_grid.max()])
        plt.colorbar(plot,ax=ax)

        img = physops.magnitude(src).astype(np.float64)
        ax = fig.add_subplot(223)
        ax.title.set_text("MAGNITUDE")
        # ax.title.set_color(color="white")
        plot = plt.imshow(img,cmap="gray",extent=[src.x_grid.min(),src.x_grid.max(),src.y_grid.min(),src.y_grid.max()])
        plt.colorbar(plot,ax=ax)


        img = physops.phase(src).astype(np.float64)
        ax = fig.add_subplot(224)
        ax.title.set_text("PHASE")
        # ax.title.set_color(color="white")
        plot = plt.imshow(img,cmap="gray",extent=[src.x_grid.min(),src.x_grid.max(),src.y_grid.min(),src.y_grid.max()])
        plt.colorbar(plot,ax=ax)

        plt.ion()
        plt.show()


def normalize(src,output_type=np.float64):
    img = (np.asarray(src) / np.max(src))
    return img.astype(output_type)



def normalizeAndBin(src,max_count=255,cast_type=np.uint8):
    """
    normalizes and bins the bins the input image to a given bit depth and max_count

    input::
        src (np.ndarray): input image
        max_count (int,float): coefficient to multiple normalized array by
        cast_type (numpy.dtype): numpy dtype the final array is casted to

    return::
        img (np.ndarray): normalized and binned image

    """
    src = src.astype(np.float32)
    src = ( src / src.max() ) * max_count
    src = src.astype(cast_type)
    return src


def quickImageView(img,normalize_and_bin=False):
    """
    quickly displays the image using a PIL Image Viewer

    input::
        img (np.ndarray): input image you want to view
        normalize_and_bin (bool): boolean value indicating whether or not to normalize and bin the image

    return::
        None
    """
    if normalize_and_bin:
        img = normalizeAndBin(img,max_count=255,cast_type=np.uint8)
    if len(img.shape) > 2:
        img = np.flip(img,2)
    img = Image.fromarray( img )
    img.show("quickView image")
