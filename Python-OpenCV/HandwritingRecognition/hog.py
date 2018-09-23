from skimage import feature

# HOG: Histogram of Oriented Gradients
# operate on the gradient magnitude of an image
# this is similar to edge detection...
# HOG computes histograms on a dense grid of
# uniformly-spaced cells that can overlap and be
# contrast normalized. (can also find people in imgs)
# (SIFT computes over the orientation of the edges
# in small, localized areas of the image).


class HOG:
    def __init__(self, orientations=9, pixelspercell=(8, 8),
                 cellsperblock=(3, 3), transform=False):
        # parameters:
        # orientations- how many gradient orientations (bins)
        #   will be in each histogram
        # pixelspercell-the image will be partitioned into cells
        #   each one is the square of this value, a histogram
        #   of gradient magnitudes is computed for each cell
        # cellsperblock- normalize each of the histograms according
        #   to the number of cells that fall into each block
        # transform-apply a power law compression- take the log/
        #   square-root of the image input
        self.orientations = orientations
        self.pixelspercell = pixelspercell
        self.cellsperblock = cellsperblock
        self.transform = transform

    def describe(self, image):
        hist = feature.hog(image,
                           orientations=self.orientations,
                           pixels_per_cell=self.pixelspercell,
                           cells_per_block=self.cellsperblock,
                           transform_sqrt=self.transform)
        return hist
