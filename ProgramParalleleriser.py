import numpy as np
import os
import rpmClass_Stable as rpm


width_list = np.linspace(20e-9, 500e-9, 25)
gap_list = np.linspace(20e-9, 150e-9, 14)
Hcstd_list = np.linspace(0.0000001, 0.1, 26)
Happ_list = np.linspace(0.095, 0.105, 11)
latticesize_list = np.array([5,10,12,15,18,20,22,25,30])
initialstate_list = np.array(['sat', 'rand', 'ground'])
print(width_list, Hcstd_list, Happ_list)
i = 0


Hc = 0.1					#Coercive Field
Hc_std1 = 0.1


bar_length = 400e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 15e-9		#Bar thickness in m
bar_width = 200e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 830e3)

#Lattice Parameters

'''
with open('SquareSizeTemplate.py', 'r') as r:
	content = r.read()
	r.close()

folderloc = os.path.join(os.getcwd(), 'Square_SizeDependence' % locals())
if not os.path.exists(folderloc):
    os.makedirs(folderloc)

for initialstate in initialstate_list:
	for size in latticesize_list:
		for n in np.arange(1, 101):
			with open(os.path.join(folderloc, 'SquareSize.%(i)d.py' % locals()), 'w') as f:
				f.write(content)
				f.write('\n')
				f.write('size = %(size)i \n' %locals())
				f.write('lattice = rpm.ASI_RPM(size,size,bar_length = bar_length,vertex_gap = vertex_gap, bar_thickness = bar_thickness,bar_width = bar_width, magnetisation = magnetisation)\n')
				f.write('lattice.square(Hc, QD) \n')
				if initialstate == 'sat':
					print('Do nothing')
				elif initialstate == 'rand':
					f.write('lattice.randomMag() \n')
				elif initialstate == 'ground':
					f.write('lattice.squareGroundState() \n')
				else:
					print('Please use one of the available initial states (sat, rand, ground)')
					break
				f.write('differentName = "Square_init%(initialstate)s_Size%(size)d_n%(n)d" \n' %locals())
				f.write('folderloc = os.path.join(folder, differentName) \n')
				f.write('lattice.fieldSweepAdaptive(Hmax,steps, field_angle, loops = 15, n=5, folder = folderloc, q1 = True) \n'%locals())
				i+=1
'''


'''
size = 20

with open('SquareHappQDTemplate.py', 'r') as r:
	content = r.read()
	r.close()

folderloc = os.path.join(os.getcwd(), 'Square_HappQD' % locals())
if not os.path.exists(folderloc):
    os.makedirs(folderloc)

for initialstate in initialstate_list:
	for QD in Hcstd_list:
		for Happ in Happ_list:
			for n in np.arange(1, 11):
				with open(os.path.join(folderloc, 'SquareHapp_QD.%(i)d.py' % locals()), 'w') as f:
					f.write(content)
					f.write('\n')
					f.write('lattice = rpm.ASI_RPM(size,size,bar_length = bar_length,vertex_gap = vertex_gap, bar_thickness = bar_thickness,bar_width = bar_width, magnetisation = magnetisation)\n')
					f.write('lattice.square(Hc, %(QD)e) \n' %locals())
					if initialstate == 'sat':
						print('Do nothing')
					elif initialstate == 'rand':
						f.write('lattice.randomMag() \n')
					elif initialstate == 'ground':
						f.write('lattice.squareGroundState() \n')
					else:
						print('Please use one of the available initial states (sat, rand, ground)')
						break
					f.write('differentName = "Square_init%(initialstate)s_QD%(QD)e_Hmax%(Happ)e_n%(n)d" \n' %locals())
					f.write('folderloc = os.path.join(folder, differentName) \n')
					f.write('lattice.fieldSweepAdaptive(%(Happ)e,steps, field_angle, loops = 15, n=5, folder = folderloc, q1 = True) \n'%locals())
					i+=1
'''


size = 5					#Define the size of the lattice
lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)

lattice.tetris(Hc, Hc_std1)
#lattice.save('SquareCheckLattice20x20')


#lattice.square(Hc, Hc_std1)
#lattice.save('2SquarePeriodDoublingLattice20x20')
#lattice.square(Hc, Hc_std1)
#lattice.save('3SquarePeriodDoublingLattice20x20')
#lattice.square(Hc, Hc_std1)
#lattice.save('4SquarePeriodDoublingLattice20x20')
#lattice.square(Hc, Hc_std1)
#lattice.save('5SquarePeriodDoublingLattice20x20')

with open('Tetris20x20_PeriodDouble_template.py', 'r') as r:
	content = r.read()
	r.close()
folderloc = os.path.join(os.getcwd(), 'Tetris-45_PeriodDouble' % locals())
if not os.path.exists(folderloc):
    os.makedirs(folderloc)

for n in np.arange(1,11):
	for width in width_list:
		for QD in Hcstd_list:
			with open(os.path.join(folderloc, 'Tetris5x5_Happ-45.%(i)d.py' % locals()), 'w') as f:
				f.write(content)
				f.write('\n')
				#f.write('lattice.load(os.path.join(folder,"SquareCheckLattice20x20.npz")) \n' %locals())
				f.write('lattice.changeQuenchedDisorder(%(QD)f) \n' %locals())
				f.write('lattice.changeWidth(%(width)e) \n' %locals())
				f.write('differentName = "TetrisPD-45_QD%(QD)e_Width%(width)e_count%(n)d" \n' %locals())
				f.write('folderloc = os.path.join(folder, differentName) \n')
				f.write('lattice.fieldSweepAdaptive(Hmax,steps, field_angle, loops = 15, n=5, folder = folderloc, q1 = True) \n'%locals())
				i+=1
