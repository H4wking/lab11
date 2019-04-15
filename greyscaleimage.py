from arrays import Array2D


class GrayscaleImage:
    def __init__(self, nrows, ncols):
        self._grid = Array2D(nrows, ncols)
        self.clear(0)

    def clear(self, value):
        for i in range(self._grid.num_rows()):
            for j in range(self._grid.num_cols()):
                self.setitem(i, j, value)

    def setitem(self, row, col, value):
        self._grid[row, col] = value

    def getitem(self, row, col):
        return self._grid[row, col]

    def width(self):
        return self._grid.num_cols()

    def height(self):
        return self._grid.num_rows()
