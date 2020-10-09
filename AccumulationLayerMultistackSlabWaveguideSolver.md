# Accumulation Layer Multistack Slab Waveguide Solver

## Organisation

* root treated as current working directory.
* dir_paths is a json config file containing the relevant directory paths.
* params is a json config file containing the following parameters:
  * lambda0 = incident wavelength (nm)
  * Substrate = [refractive index, extinction coefficient, thickness (nm)]
  * Waveguide = [refractive index, extinction coefficient, thickness (nm)]
  * Layer1 = [refractive index, extinction coefficient, thickness (nm)]
  * LayerN = [refractive index, extinction coefficient, thickness (nm)
  * Cover = [refractive index, extinction coefficient, thickness (nm)]
* Where LayerN is any layer between waveguide and cover.
* These parameters (params) are then unpacked into variables using the operator.itemgetter library function
* The date/time string (dt_string) for the moment the code is run is called. This is of the form "YYYYMMDDhhmm". The date/time string is used for file output names.
* Finally, set the data outpath and use the check_dir_exists function to ensure that the path exists.

## Parameters

* alt is given as the accumulation layer thickness and is a set range dependent on the material in question. This is a varying parameter that is the key to this particaular waveguide solver.
* Using the alt range, we set the thicknesses of the waveguide layers, where the accumulation layer is a sub-section of layer 1 and the total thickness remains constant.
* We then set the refractive indices of the layers using the params dictionary, and use them to give the simulation a starting refractive index guess range.
* Calculate the incident k-vector for the incident wavelength and use it to calculate the propagation (beta) into the waveguide.
* Finally we set up the output matrices, which have the shape of accumulation layer thickness against the propagation guesses in (which is the shape of the graph output too).

## Calculations

* We loop through the various thickness arrays, and the propagation in guesses, given the indices of each matrix (x, y) respectively. This allows us to index the output graph.
* From there we use the multilayer to calculate the propagation out matrix with the input parameters.
* Then we use the Newton Raphson method to calculate the effective index (minimum in the propagation matrix).

## Output Organsiation

* n_textstring and out_n_textstring create a string of the respective refractive indices used.
* The title string uses the n_textstring and also uses the waveguide and layer 1 thickness for indication.
* The outname/outxt_string(s) are used for the effective index txt file and the plotted graph file, and use th date/time string to indicate the order in which the results were found.

## Data Processing

* We use the effective_index_finder function to average all of the calculated effective index values and output a csv containing all the possible effective indices with respect to the accumulation layer thickness.
