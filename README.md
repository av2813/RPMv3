# RPMv3

## Getting Started
You need to have installed either python 2 or 3 with the following packages:
	- numpy
	- matplotlib
	- scipy
Installing a scientific python such as anaconda should give you all the packages that 
you will need


##Running the tests

#To Do
```

```
You have a general class that is referred to as the RPM_ASI which you define the properties
of the material and the lattice. It is possible to change and update all the properties 
of the class, such as, lattice gap, Msat, etc.




##List of functions:

#Loading and Saving
	- save
	- load
	- loadSpinWrite

#Lattice makers:
	- square
	- brickwork
	- tiltedSquare
	- kagome
	- shortShakti
	- longShakti
	- tetris

#Plotting functions
    - graph: Plots a quiver graph that shows the Coercive field, counts and vertex state
    - graphCharge: Plots a quiver with the charge of the vertex for kagome and tetris
    - Correlation: Plots the local corration between spins based on the surrounding microstates
    - fieldPlot: Plots the local field at each point on the lattice and vertex. Colour is 
                proportional to the strength of the field
    - vertexTypeMap: Plots the vertex type for a square lattice
    - Animation: Can give a field sweep field and it will display an animation of 
                how the bars flip over the field sweep
    - localPlot: Plots the lattice around position (x,y) with radius n
    - fieldSweepAnimation: Plots an animation of the field s
    - localCorrelation: Plots the local correlation


#Magnetic ordering functions
	- magneticOrdering
	- structureFactor

#Field Sweep functions
	- relax
	- hysteresis
	- fieldSweep
	- appliedFieldSweep
	- searchRPM_monte
	- searchRPM_single
	- searchRPM_multiple
	- demagnetisationProtocol

#Field Sweep Analysis functions
	- fieldSweepAnalysis
	- analysisAppliedFieldSweep
	- analysisSingleFlip
	- analysisMC
	- plotCorrelation
	- plotMagnetisation
	- plotMonopole
	- plotVertex

#Field functions
	- dumbbell
	- dipole
	- fieldreturn
	- fieldCalc
	- Hlocal2
	- effectiveCoercive

#Histograms
	- localFieldHistogram
	- effectiveCoerciveHistogram
	- coerciveHistogram
	- latticeFieldHistogram
	- vertexHistogram
	- correlationHistogram

#Lattice properties functions
	- netMagnetisation
	- countSpins
	- monopoleDensity
	- returnUnitCellLen
	- vertexTypePercentage
	- returnLattice
	- demagEnergy

	- correlation


#Lattice manipulation functions
	- clearLattice
	- randomMag
	- flipSpin
	- changeLength
	- changeWidth
	- changeVertexgap
	- changeinteractionType
	- changeMagnetisation
	- changeHc
	- makeMonopole
	- squareMonopoleState
	- squareGroundState
	- squareType3State
	- flipAll
	- fixEdges
	- changeQuenchedDisorder
	- resetCount
	- subtractCount
	- changeQuenchedDisorder

