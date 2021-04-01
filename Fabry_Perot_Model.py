import os

root = os.getcwd()

'''
Information taken from:
https://discovery.ucl.ac.uk/id/eprint/1447253/1/PhD_theses_master.pdf

The free spectral range defined in terms of wavelength is derived by equating
the difference in phase between successive reflectance minima's which is 2pi,
with that for the derivative of the phase with respect to wavelength and
rearranging to get it in terms of delta lambda. The final equation is:

FSR = ((lambda_0)**2)/2nl

where lambda_0 is the wavelength corresponding to the first reflectance minima,
and nl is the optical thickness. This expression shows that the FSR decreases
with increasing cavity thickness, due to the inverse relationship. The FSR in
terms of phase will always be 2pi.

The phase, psi, is defined as:

psi = (4*pi*n_c*l)/lambda

where nl is the optical path length, n_c is the refractive index of the cavity,
l is the physical path length, and lambda is the wavelength. The phase
difference between each round trip is therefore constant. The phase in the Airy
function:

P_ref = F * sin(psi/2)**2 / (1 + Fsin(psi/2)**1)

leads to reflectance minima's at particular values of phase.

As the mirror reflectivities increase, the reflectivity peaks become narrower.
This is because the ability of the FPI cavity to retain energy is greater as
the mirror reflectivity is increased. As R increases, F increases, resulting in
a narrow reflectivity peak. The reflected power is a maximum when the criterion
for constructive interference is sin**2(psi/2)=1, therefore psi=(2p+1)pi, where
p is an integer, resulting in the relation:

p*lambda/4 = nl

Similarly for destructive interference where psi=2*pi*p results in:

p*lambda/2 = nl

with p = 1, 2, 4, 6...m.

Assuming the refractive index n_c as l, the wavelength has to be multiples of a
quarter of the optical thickness for constructive interference. For destructive
interference, the wavelength had to be multiples of half of the optical
thickness, so that the phase difference is pi between the field reflected off
the incident mirror and the electric fields which have undergone a number of
round transits in the cavity.
'''
