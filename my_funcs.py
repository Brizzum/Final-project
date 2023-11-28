import numpy as np

# averaginf a circular variable
def Wdir_averaging(Theta):
    Sa = np.mean(np.sin(np.radians(Theta)))
    Ca = np.mean(np.cos(np.radians(Theta)))
    ThetaAvg = np.mod((180/np.pi)*(np.arctan2(Sa,Ca)),360)

    ThetaStd = np.sqrt(1-Sa**2-Ca**2)

    return ThetaAvg, ThetaStd


# define function alpha=fn(De/distance)
def disturbed_sector(Le,De):
    alpha = 1.3*np.arctan(2.5*De/Le + 0.15)*180/np.pi + 10
    #convert to degrees
    return alpha
