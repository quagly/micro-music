#!/usr/bin/env python

# following quickstart
# https://numpy.org/devdocs/user/quickstart.html

import numpy as np

# basic attributes
my_array = np.arange(15).reshape(3, 5)

print(f'my_array shape is: {my_array.shape}')
print(f'my_array number of dimensions is: {my_array.ndim}')
print(f'my_array datatype is: {my_array.dtype}')
print(f'my_array datatype takes {my_array.itemsize} bytes')
print(f'my_array number of elements is: {my_array.size}')

# creation
# create from list
create_ints = np.array([2, 3, 4])
# type is inferred
print(f'create_ints datatype is: {create_ints.dtype}')
create_floats = np.array([1.2, 3.5, 5.1])
print(f'create_floats datatype is: {create_floats.dtype}')


# create two dimensional
create_two_dims = np.array([(1.5, 2, 3), (4, 5, 6)])
print(f'create_two_dims number of dimensions is: {create_two_dims.ndim}')
print(f'create_two_dims datatype is: {create_two_dims.dtype}')

# specify datatype rather than infer
create_complex = np.array([[1, 2], [3, 4]], dtype=complex)
print(f'create_complex datatype is: {create_complex.dtype}')
print(f'{create_complex.dtype} datatype takes {create_complex.itemsize} bytes')

# initialize size without data
# create 3x4 matrix of zeros
create_zeros = np.zeros((3, 4))
# 2x3x4 matrixs of ones with int16 datatype
create_ones = np.ones((2, 3, 4), dtype=np.int16)
# empty creates "random" numbers
# 2x3 matrix of "random"
create_random = np.empty((2, 3))
print(f'empty creates random elements of type {create_random.dtype}')

# arange ( think array range ) generates data
# create array [10,30) so missing 30
create_byfives = np.arange(10, 30, 5)

# when using floats better to use linspace to avoid precision issues
# which cause unpredictable number of elements
# get nine numbers between 0 and 2
create_linspace = np.linspace(0, 2, 9)
# 100 elements between 0 and 2π
create_radians = np.linspace(0, 2 * np.pi, 100)
get_sin = np.sin(create_radians)
# print(f'sin of 100 points of the circle are: {get_sin}')

# basic operations
array_one = np.array([20, 30, 40, 50])
print(f'array_one is: {array_one}')
array_two = np.arange(4)
print(f'array_two is: {array_two}')
array_minus = array_one - array_two
print(f'array one minus two is: {array_minus}')
array_power = array_one ** 2
print(f'array one squared is: {array_power}')
array_calc = 10 * np.sin(array_one)
print(f'array one 10*sin: {array_calc}')
array_test = array_one < 35
print(f'array one less than 35 test is: {array_test}')

# stats
print(f'sum of array_one is: {array_one.sum()}')
print(f'min of array_one is: {array_one.min()}')
print(f'max of array_one is: {array_one.max()}')

# universal functions operate on every element of an array
# may such functions.  I may want to use np.re, np.where
print(f'sqrt of array_one is: {np.sqrt(array_one)}')
print(f'e to power array_two is: {np.exp(array_two)}')
print(f'array_one plus array_two is: {np.add(array_one, array_two)}')

# one dimensional arrays act a lot like lists
print(f'second element of array_one is: {array_one[1]}')
print(f'second throuh forth elements of array_one are: {array_one[1:4]}')





print



