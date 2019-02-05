# R2C2_BEXUS_Simulations

This project contains all components important for the simulations for the BEXUS experiment R2C2. An overview of the concept is given in the image Software_diagram.pdf. The concept is based on an existing simulation. A paper describing this simulation in detail can be found in the directory "Papers"


*** Goals of the simulation ***
The simulation shall help predict the behaviour of the chaff clouds and combine this with the behaviour of the radars and will be used to predict the success of the experiment based on different changeable parameters. Examples are:
- How much chaff leads to what size of cloud? At what densities?
- What size/shape of chaff leads to what drop speeds?
- How strong signals can a certain radar measure from the chaff cloud?
- What time/spatial resolutions can be acheived?


*** Organization ***
This project currently contains three directories:
- "Papers" contains the most important papers on which the simulation is based. 
- "Simulation_code" contains the whole existing python code for the simulation. As well as a second README explaining the code in more detail.
- "Wind_Model" contains Radiosonde data sets, code for analysis of this data and a file with the results. This can be used for the simulation of the winds during the experiment.


*** ToDo's ***
- Find reliable lookup table for the drag coefficient or the axial- and normal-force coefficients in relation to the Reynolds number and the angle of attack.
OR find fitting values for the Drag coefficient and generate the starting values in a Monte Carlo simulation.
- Fully create a set of chaff pieces with all needed properties set.
- Run a simulation of the motion of these pieces.
- Add the wind background to the simulation.
- Continue to implement everything that is red in the Software_diagram.pdf.


*** Main Problems ***
- It is very hard to figure out the correct initial conditions for different types of chaff. Many parameters will have to be adjusted to the currently tested conditions.
- The generation for meaningful initial values for the reynolds number and the angle of attack respectively for the drag coefficient used lookup tables for the aerodynamic coefficients in the past. Unfortunately these lookup-tables could not be found until now. (Even though no efforts have been made to actually contact people who might have access to the resources of the original research.



