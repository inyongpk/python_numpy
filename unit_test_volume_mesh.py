import sys
import numpy as np

"""  
Function get_volume_mesh(mesh) returns volume of a set of triangular facets, mesh.
Algorithm in "Efficient feature extraction for 2D/3D objects in mesh representation", 
Cha Zhang and Tsuhan Chen, Dept. of ECE, Carnegie Mellon University
"""
def get_volume_mesh(mesh):
    volume = 0.0

    # tfvertex is an array of 3 vertexes of a trianglular facet
    for tfvertex in mesh: 
        # Refer to https://en.wikipedia.org/wiki/Tetrahedron#Volume
        tetvolume = (np.inner(tfvertex[0],np.cross(tfvertex[1],tfvertex[2])))/6.0
        volume += tetvolume

    return volume

# Main 
mesh = np.load('unit_cube_qppp.npy')
print 'Shape:  ', mesh.shape
print 'Size:   ', mesh.size
volume = get_volume_mesh(mesh)
# error tolerance is 0.00000000001
if (volume - 1.0 < 0.00000000001):
   print 'get_volume_mesh works correctly.'
else:
   print 'get_volume_mesh does not work correctly.'

