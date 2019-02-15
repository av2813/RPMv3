import rpmClass_Stable as rpm
import numpy as np
import matplotlib.pyplot as plt
from importlib import *
import os
import seaborn as sns

reload(rpm)


folder = r'D:\RPM_Rapid\TetrisPeriodDouble\PeriodDoublingData_QD1.000000e-07_Width4.000000e-08_Count1'

initial_file = r'InitialRPMLattice_Hmax1p414214e-01_steps10_Angle7p853982e-01_neighbours5_Loops10.npz'

Lattice = rpm.ASI_RPM(1,1)

Lattice.load(os.path.join(folder, initial_file))

field_angle=45.
Hmax = 0.1/np.cos(np.pi/4)

#savefolder = r'C:\Users\av2813\Desktop\RPM_tests'
#differentName = "PeriodDoublingData_QD1.000000e-07_Width4.000000e-08_Count1_30_Random3_finer20steps" 
#folderloc = os.path.join(savefolder, differentName) 
#Lattice.fieldSweep(Hmax, 20, field_angle, n=5, loops=30, folder = folderloc, q1 = True) 



import numpy as np

class pbcarray(np.ndarray):
    """
    A ndarray with periodic boundary conditions when slicing (a.k.a. wrap).
    Any rank is supported.
    Examples
    --------
    2D array for semplicity of visualization, any rank should work.
    >>> dim = 3
    >>> A = np.zeros((dim,dim),dtype=int)
    >>> for i in range(dim):
    ...     A[i,i] = i+1
    >>> A = pbcarray(A)
    >>> print(A)
    [[1 0 0]
     [0 2 0]
     [0 0 3]]
    >>> print(A[-dim:,:2*dim])
    [[1 0 0 1 0 0]
     [0 2 0 0 2 0]
     [0 0 3 0 0 3]
     [1 0 0 1 0 0]
     [0 2 0 0 2 0]
     [0 0 3 0 0 3]]
    """

    def __new__(cls, pos):
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(pos).view(cls)
        # add the new attribute to the created instance
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):

        if obj is None:
            return

    def __getitem__(self, index):
        """
        Completely general method, works with integers, slices and ellipses,
        Periodic boundary conditions are taken into account by rolling and
        padding the array along the dimensions that need it.
        Slices with negative indexes need special treatment.
        """
        shape_ = self.shape
        rank = len(shape_)

        slices = _reconstruct_full_slices(shape_, index)
        # Now actually slice with pbc along each direction.
        newarr = self
        slice_tup = [slice(None)]*rank

        for idim, sli in enumerate(slices):
            if isinstance(sli, int):
                slice_tup[idim] = sli % shape_[idim]
            elif isinstance(sli, slice):
                roll, pad, start, stop, step = _check_slice(sli, shape_[idim])
                # If the beginning of the slice does not coincide with a grid point
                # equivalent to 0, roll the array along that axis until it does
                if roll > 0:
                    newarr = np.roll(newarr, roll, axis=idim)
                # If the span of the slice extends beyond the boundaries of the array,
                # pad the array along that axis until we have enough elements.
                if pad > 0:
                    pad_tup = [(0, 0)] * rank
                    pad_tup[idim] = (0, pad)
                    newarr = np.pad(newarr, pad_tup, mode='wrap')
                slice_tup[idim] = slice(start, stop, step)

        slice_tup = tuple(slice_tup)

        return np.ndarray.__getitem__(newarr, slice_tup)


def _reconstruct_full_slices(shape_, index):
    """
    Auxiliary function for __getitem__ to reconstruct the explicit slicing
    of the array if there are ellipsis or missing axes.
    """
    if not isinstance(index, tuple):
        index = (index,)
    slices = []
    idx_len, rank = len(index), len(shape_)

    for slice_ in index:
        if slice_ is Ellipsis:
            slices.extend([slice(None)] * (rank+1-idx_len))
        elif isinstance(slice_, slice):
            slices.append(slice_)
        elif isinstance(slice_, (int)):
            slices.append(slice_)

    sli_len = len(slices)
    if sli_len > rank:
        msg = 'too many indices for array'
        raise IndexError(msg)
    elif sli_len < rank:
        slices.extend([slice(None)]*(rank-sli_len))

    return slices

def _check_slice(sli, dim):
    """
    Check if the current slice needs to be treated with pbc or if we can
    simply pass it to ndarray __getitem__.
    Slice is special in the following cases:
    if sli.start < 0 or > dim           # roll (and possibly pad)
    if sli.stop > dim or < 0            # roll (and possibly pad)
    if abs(sli.stop - sli.start) > dim  # pad
    """
    _roll = 0
    _pad = 0

    step = sli.step or 1
    start = (0 if step > 0 else dim) if sli.start is None else sli.start
    stop = (dim if step > 0 else 0) if sli.stop is None else sli.stop
    span = (stop - start if step > 0 else start - stop)

    if span <= 0 :
        return _roll, _pad, sli.start, sli.stop, sli.step

    lower = min(start, stop)
    upper = max(start, stop)
    _start = 0 if step > 0 else span
    _stop = span if step > 0 else 0
    if span > dim:
        _pad = span - dim
        _roll = -lower % dim
    elif lower < 0 or upper > dim:
        _roll = -lower % dim
    else:
        _start = sli.start
        _stop = sli.stop
    return _roll, _pad, _start, _stop, step



grid = Lattice.returnLattice()


grid2 = np.tile(grid, (3,3))

def periodicBC(array):
	#new_array = np.tile(array, (3,3))
	xlen, ylen, chars = np.shape(array)
	testarray = np.hstack((array, array, array))
	new_array = np.vstack((testarray, testarray, testarray))
	print(testarray, np.shape(testarray))
	#print(array[:,:,0] - array[:,:,0].max())
	#print(np.shape(new_array), xlen, ylen)
	new_array[:xlen,ylen:2*ylen,0] = array[:,:,0] - array[:,:,0].max()
	new_array[2*xlen:,ylen:2*ylen,0] = array[:,:,0] + array[:,:,0].max()
	new_array[xlen:2*xlen,:ylen,1] = array[:,:,1] - array[:,:,1].max()
	new_array[xlen:2*xlen,2*ylen:,1] = array[:,:,1] + array[:,:,1].max()
	new_array[2*xlen:,2*ylen:,0:2] = array[:,:,0:2] + array[:,:,1].max()
	new_array[:xlen,2*ylen:,0] = array[:,:,0] - array[:,:,1].max()
	new_array[:xlen,2*ylen:,1] = array[:,:,1] + array[:,:,1].max()
	new_array[:xlen,:ylen,0:2] = array[:,:,0:2] - array[:,:,1].max()
	new_array[:xlen,:ylen,0:2] = array[:,:,0:2] - array[:,:,1].max()
	new_array[2*xlen:,:ylen:,0] = array[:,:,0] + array[:,:,0].max()
	new_array[2*xlen:,:ylen,1] = array[:,:,1] - array[:,:,1].max()

	return(new_array)

grid2 = periodicBC(grid)
data = grid2
new_array = [tuple(row) for row in data]
uniques = np.unique(new_array)
print(uniques)
#grid2 = np.roll(grid, 13, axis = 0)
#print(grid2)

Lattice2 = rpm.ASI_RPM(lattice = grid2)

Lattice2.graph()
#Lattice.graph()
#Lattice2.graphCharge()
