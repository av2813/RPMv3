import numpy as np
import os
import rpmClass_Stable as rpm


width_list = np.linspace(20e-9, 500e-9, 25)
Hcstd_list = np.linspace(0.0000001, 0.1, 26)
Happ_list = np.linspace(0.095, 0.105, 11)
print(width_list, Hcstd_list, Happ_list)
i = 0


Hc = 0.1					#Coercive Field
Hc_std1 = 0.1


bar_length = 400e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 15e-9		#Bar thickness in m
bar_width = 80e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 830e3)

#Lattice Parameters
size = 20					#Define the size of the lattice
lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)

#lattice.square(Hc, Hc_std1)
#lattice.save('1SquarePeriodDoublingLattice20x20')
#lattice.square(Hc, Hc_std1)
#lattice.save('2SquarePeriodDoublingLattice20x20')
#lattice.square(Hc, Hc_std1)
#lattice.save('3SquarePeriodDoublingLattice20x20')
#lattice.square(Hc, Hc_std1)
#lattice.save('4SquarePeriodDoublingLattice20x20')
#lattice.square(Hc, Hc_std1)
#lattice.save('5SquarePeriodDoublingLattice20x20')

with open('SquarePeriodDoublingTemplate.py', 'r') as r:
	content = r.read()
	r.close()

folderloc = os.path.join(os.getcwd(), 'Square_PeriodDoublev2' % locals())
if not os.path.exists(folderloc):
    os.makedirs(folderloc)

for width in width_list:
	for Hc_std in Hcstd_list:
		for count in np.arange(1,6):
			with open(os.path.join(folderloc, 'SquareRAND20x20_PeriodDouble.%(i)d.py' % locals()), 'w') as f:
				f.write(content)
				f.write('lattice.load(os.path.join(folder,"%(count)dSquarePeriodDoublingLattice20x20.npz")) \n' %locals())
				f.write('lattice.randomMag() \n')
				f.write('lattice.changeQuenchedDisorder(%(Hc_std)f) \n' %locals())
				f.write('lattice.changeWidth(%(width)e) \n' %locals())
				f.write('differentName = "PeriodDoublingData_QD%(Hc_std)e_Width%(width)e_Count%(count)d" \n' %locals())
				f.write('folderloc = os.path.join(folder, differentName) \n')
				f.write('lattice.fieldSweep(Hmax, 10, field_angle, n=5, loops=10, folder = folderloc, q1 = True) \n')
				i+=1
