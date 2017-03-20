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
# Error tolerance, 1e-10 is chosen for a unit test.
error_tolerance = 0.0000000001
print 'Error tolerance: ', error_tolerance

test_array_meshes = [['unit_cube_qppp.npy', 1.0], ['shell.npy', 3.6586764273115655], ['Robot_Maker_Faire_65pc.npy', 43677.42582662092]]

for array_mesh in test_array_meshes:
    mesh = np.load(array_mesh[0])
    print 'Shape:  ', mesh.shape
    print 'Size:   ', mesh.size
    volume = get_volume_mesh(mesh)
    print 'Target volume:       %.16f' %array_mesh[1]
    print 'Calculated volume:   %.16f' %volume
    if (abs(volume - array_mesh[1]) < error_tolerance):
       print 'get_volume_mesh works correctly with %s.' %array_mesh[0]
    else:
       print 'get_volume_mesh does not work correctly with %s.' %array_mesh[0]

