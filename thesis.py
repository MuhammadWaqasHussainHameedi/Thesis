from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

# Open a FITS file
Fits_file=['E:\DATA\data thesis\spec-0266-51630-0004.fits','E:\DATA\data thesis\spec-0266-51630-0001.fits','E:\DATA\data thesis\spec-0266-51630-0002.fits','E:\DATA\data thesis\spec-0266-51630-0006.fits']
#for spectral lines
Spectra= { 6565.61 :'H_alpha', 4862.68 :'H_beta',4342.68:'H_gamma'}
plt.figure(figsize=(10,6))
for a in Fits_file :
#Access the data in the primary HDU (Header Data Unit)
#Hdu.open work in single so put in for loop and use x
#SDSS is usually in first extension
    hdulist=fits.open(a)
    data = hdulist[1].data
    flux=data['flux']
    loglam=data['loglam']
    wavelength=10**loglam
    plt.plot(wavelength,flux,drawstyle='steps-mid',label=a.split('\\')[-1])#label=x.split('\\')[-1]) is because it only contain file name
    hdulist.close()
#for spectral lines
for wavelength,Line_name in Spectra.items():#because having multiple elements therefor use loop
    plt.axvline(x=wavelength,color='green',linestyle='--',label=f"{Line_name},({wavelength})")
#plot setting
plt.legend(title="fits files")
plt.xlabel('Wavelength(A)')
plt.ylabel('flux')
plt.grid(True)
plt.legend()
plt.show()
