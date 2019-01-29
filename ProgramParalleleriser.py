import numpy as np
import os
import rpmClass_Stable as rpm


with open(os.path.join(os.getcwd(),'TetrisPeriodDoublingTemplate.py'), 'r') as r:
	content = r.read()
	r.close()

width_list = np.linspace(50e-9, 500e-9, 10)
i = 0


Hc = 0.1					#Coercive Field
Hc_std = 0.01


bar_length = 600e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 20e-9		#Bar thickness in m
bar_width = 80e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 830e3)

#Lattice Parameters
size = 5					#Define the size of the lattice
lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)

lattice.tetris(Hc, Hc_std)
lattice.save('TetrisPeriodDoublingLattice20x20')


for width in width_list:
	lattice.load()
	for count in np.arange(1,4):
		with open('Tetris20x20_PeriodDouble.%(i)d.py' % locals(), 'w') as f:
			f.write(content)
			f.write('lattice.changeWidth(%(width)e) \n' %locals())
			f.write('differentName = QD%(Hc_std)e_Width%(width)e_%(count)d' %locals())
			f.write('folderloc = os.path.join(folder, differentName)')
			f.write('lattice.fieldSweep(Hmax, 10, field_angle, n=5, loops=10, folder = folderloc, q1 = True)')
			