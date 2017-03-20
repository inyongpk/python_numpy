1. volume_mesh.py 
	It gets volume of a set of triangular facets, mesh.
	It has a npy file as its argument which has an array of triangular facets.
	<example>
	  python volume_mesh.py unit_cube_qppp.npy

2. unit_test_volume_mesh.py 
	It is a unit test module for get_volume_mesh() function.
	It tests get_volume_mesh() with unit_cube_qppp.npy.
	unit_cube_qppp.npy has a mesh whose volume is a unit cube, 1.0.

3. get_volume_mesh(mesh)
   It returns volume of an array of triangular facets, mesh that is an argument.
   It sums volume of tetrahedrons that consist of origin (0,0,0) and a triangular facet in mesh.

4. Reference
	[1] "Efficient feature extraction for 2D/3D objects in mesh representation", 
	     Cha Zhang and Tsuhan Chen, Dept. of ECE, Carnegie Mellon University
        [2] https://en.wikipedia.org/wiki/Tetrahedron#Volume
5. Versions 
	[1] Python 2.7.5
	[2] Numpy 1.6.2
