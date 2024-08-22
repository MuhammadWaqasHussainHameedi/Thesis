from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
#for single
'''hdulist = fits.open('E:\DATA\data thesis\spec-0266-51630-0001.fits')
# Access the data in the primary HDU (Header Data Unit)
#SDSS is usually in first extension
data = hdulist[1].data
flux=data['flux']
loglam=data['loglam']
wavelength=10**loglam

plt.figure(figsize=(10,6))
plt.plot(wavelength,flux,drawstyle='steps-mid')
plt.xlabel('Wavelength(A)')
plt.ylabel('flux')
plt.grid(True)
plt.legend()
plt.show()
hdulist.close()'''


#calling individualy
# Open a FITS file
'''hdulist1 = fits.open('E:\DATA\data thesis\spec-0266-51630-0001.fits')
hdulist2 = fits.open('E:\DATA\data thesis\spec-0266-51630-0002.fits')
hdulist3 = fits.open('E:\DATA\data thesis\spec-0266-51630-0004.fits')
hdulist4 = fits.open('E:\DATA\data thesis\spec-0266-51630-0006.fits')

# Access the data in the primary HDU (Header Data Unit)
#SDSS is usually in first extension
data = hdulist1[1].data
flux=data['flux']
loglam=data['loglam']
wavelength=10**loglam

data2 = hdulist2[1].data
flux2=data2['flux']
loglam2=data2['loglam']
wavelength2=10**loglam2

data3 = hdulist3[1].data
flux3=data3['flux']
loglam3=data3['loglam']
wavelength3=10**loglam3

data4= hdulist4[1].data
flux4=data4['flux']
loglam4=data4['loglam']
wavelength4=10**loglam4



plt.figure(figsize=(10,6))
plt.plot(wavelength,flux,wavelength2,flux2,wavelength3,flux3,wavelength4,flux4,drawstyle='steps-mid')
plt.xlabel('Wavelength(A)')
plt.ylabel('flux')
plt.grid(True)
plt.legend()
plt.show()
hdulist1.close()
hdulist2.close()
hdulist3.close()
hdulist4.close()'''


#Following code is looped code you dont have to call individually
# Open a FITS file
"""Fits_file=['E:\DATA\data thesis\spec-0266-51630-0004.fits','E:\DATA\data thesis\spec-0266-51630-0001.fits','E:\DATA\data thesis\spec-0266-51630-0002.fits','E:\DATA\data thesis\spec-0266-51630-0006.fits']

plt.figure(figsize=(10,6))
for x in Fits_file :
#Access the data in the primary HDU (Header Data Unit)
#Hdu.open work in single so put in for loop and use x
#SDSS is usually in first extension
    hdulist=fits.open(x)
    data = hdulist[1].data
    flux=data['flux']
    loglam=data['loglam']
    wavelength=10**loglam
    plt.plot(wavelength,flux,drawstyle='steps-mid',label=x.split('\\')[-1])#label=x.split('\\')[-1]) is because it only contain file name
    hdulist.close()

plt.legend(title="fits files")


plt.xlabel('Wavelength(A)')
plt.ylabel('flux')
plt.grid(True)
plt.legend()
plt.show()"""