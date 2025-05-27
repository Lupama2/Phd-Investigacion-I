import matplotlib.pyplot as plt
import numpy as np

def plot_results(data):
    #Plot the results of the simulation.

    fig, ax = plt.subplots(4, figsize = (8,6), dpi = 120, tight_layout = True, sharex=True)

    t = np.linspace(0, data['t'][-1], len(data['y']))

    ax[0].set_ylabel("Radio [m]")
    ax[0].plot(data['t'], data['y'][0])

    # ax[1].set_ylabel(r"$\dot R$ [m/s]")
    # ax[1].plot(data['t'], data['y'][1])

    ax[1].set_ylabel("Inestabilidad/Radio")
    ax[1].set_xlabel("Tiempo[s]")
    #ax[1].set(yscale = "log")
    ax[1].set(ylim = (-1.5,1.5))
    ax[1].plot(data['t'], data['y'][3]/data['y'][0])

    ax[2].set_ylabel("Temperatura[K]")
    ax[2].set(yscale = "log")
    ax[2].plot(data['t'], data['y'][2])

    ax[-1].set_ylabel("P Acustica[atm]")
    ax[-1].set_xlabel("Tiempo[s]")
    ax[-1].plot(T, psT/PATM)

    fig.show()