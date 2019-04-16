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
	- squareEdges
	- tiltedSquare
	- kagome
	- shortShakti
	- longShakti
	- tetris
	- squarePeriodic (should be relatively easy to make all the lattices periodic)

#Plotting functions
    - graph: Plots a quiver graph that shows the Coercive field, counts and vertex state
    - graphCharge: Plots a quiver with the charge of the vertex for kagome and tetris
    - plotCorrelation: Plots the local corration between spins based on the surrounding microstates
    - fieldPlot: Plots the local field at each point on the lattice and vertex. Colour is 
                proportional to the strength of the field
    - vertexTypeMap: Plots the vertex type for a square lattice
    - Animation: Can give a field sweep field and it will display an animation of 
                how the bars flip over the field sweep
    - localPlot: Plots the lattice around position (x,y) with radius n
    - fieldSweepAnimation: Plots an animation of the field s
    - localCorrelation: Plots the local correlation
    - fieldPlot1 (uses quiver to plot the local field)
	- fieldPlot2 (uses the streamplot function to plot the local field, slower)


#Magnetic ordering functions
	- magneticOrdering 
	- structureFactor 

#Field Sweep functions
	- relax
	- relaxAdaptive
	- relaxPeriodic
	- fieldSweep
	- fieldSweepAdaptive
	- fieldSweepPeriodic (to use on periodicSquare, similar to fieldSweepAdaptive)
	- hysteresis
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


#Field functions
	- dumbbell
	- dipole
	- fieldreturn
	- fieldCalc
	- Hlocal2
	- HlocalPeriodic (this is the important function for periodic BC)
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
	- clearLattice (remvoes the lattice)
	- randomMag (randomly flips spins in the lattice)
	- flipSpin (flip a spin at position x,y)
	- changeLength (changes the bar length)
	- changeWidth (changes the bar width)
	- changeVertexgap (changes the vertex gap)
	- changeinteractionType (can switch the interaction type from dumbbell to point dipole)
	- changeMagnetisation (changes the saturation magnetisation)
	- changeHc (changes the coercive field of a bar at a specific position)
	- makeMonopole (makes a monopole at a particular point)
	- squareMonopoleState (changes a square lattice to a monopole state)
	- squareGroundState (sets a square lattice to a ground state)
	- squareType3State (sets a square lattice to be all type 3 )
	- flipAll (reverses all the spins in the lattice)
	- fixEdges (increases the coervice field of all the edge spins to 1T)
	- changeQuenchedDisorder (adjusts the quenched disorder standard deviation while keeping the spatial distribution the same)
	- resetCount (resets the flip count of spins)
	- subtractCount ()
	- quenchedOrder (still testing, takes a pattern and tiles it onto the coercive field of the bars)

