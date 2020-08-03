# Optical_Modulators

Optical modulators repository contains a set of python scripts designed to model and design waveguide modulators.

## Multistack Slab Waveguide Solver

The multistack slab waveguide solver is based on the maths and physics contained [here](http://fotonica.intec.ugent.be/download/ocs131.pdf). The waveguide structure is simplified and considered to be invariant in the propagation direction and in the direction perpendicular to the propagation direction, i.e. only variant from bottom to top of the structure at layer interfaces. The propagation dispersion matrix is a natural progression from Maxwell's equation in 1D.

The MultistackSlabWaveguideSolver.py script in this repository makes use of this principle and utilises the multistack_optimisation function in /Functions/PhysicsMaths.py. Parameters such as waveguide/layer thicknesses and refractive indices are controlled with a json.config dictionary such that:

params = {
    "lm0" : incident wavelength(nm),
    "Sub" : [refractive index, thickness(nm)],
    "Wg" : [refractive index, thickness(nm)],
    "L1" : [refractive index, thickness(nm)],
    "L2" : [refractive index, thickness(nm)],
    "Cov" : [refractive index, thickness(nm)]
}

Where:

* lm0 = incident wavelength in nanometers
* Sub = substrate
* Wg = waveguide
* L1 = layer 1
* L2 = layer 2
* Cov = cover
* thickness in nanometers
* thickness = 0 is treated as infinite
