import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from .basic import normalize


def plot_signal_in_time(signal, frequency, title = 'Signal in time'):
    time = np.arange(0, (len(signal)/frequency), 1/frequency) / 60
    time = time[:len(signal)]
    for col in signal:
        plt.plot(time, signal[col], label=col)
    plt.xlabel('Time[min]')
    plt.ylabel('Signal')
    plt.title(title)
    plt.legend()

def plot_preprocessed_signal_in_time(signal, distance, height, title = 'Signal in time'):
    peaks, _ = find_peaks(signal, distance=distance, height=height)
    plt.plot(signal)
    plt.plot(peaks, signal[peaks], "x")
    plt.xlabel('Id')
    plt.ylabel('Signal')
    plt.title(title)

def plot_experiment(signal, experiment):
    plt.plot(signal.loc[signal['experiments'] == experiment, 'value'])
    plt.xlabel('Id')
    plt.ylabel('Signal')
    plt.title(experiment)
    plt.show()

def plot_norm_experiment(signal_polar, signal_empatica, signal_samsung, experiment, frequency_polar, frequency_empatica, frequency_samsung):
    signal_polar = signal_polar.loc[signal_polar['experiments'] == experiment, 'value']
    signal_polar = normalize(signal_polar)
    time_polar = np.arange(0, (len(signal_polar)/frequency_polar), 1/frequency_polar) / 60
    plt.plot(time_polar[:len(signal_polar)], signal_polar, label='Polar')

    signal_empatica = signal_empatica.loc[signal_empatica['experiments'] == experiment, 'value']
    signal_empatica = normalize(signal_empatica)
    time_empatica = np.arange(0, (len(signal_empatica)/frequency_empatica), 1/frequency_empatica) / 60
    plt.plot(time_empatica[:len(signal_empatica)], signal_empatica, label='Empatica')

    signal_samsung = signal_samsung.loc[signal_samsung['experiments'] == experiment, 'value']
    signal_samsung = normalize(signal_samsung)
    time_samsung = np.arange(0, (len(signal_samsung)/frequency_samsung), 1/frequency_samsung) / 60
    plt.plot(time_samsung[:len(signal_samsung)], signal_samsung, label='Samsung')
    
    plt.xlabel('Time[min]')
    plt.ylabel('Signal')
    plt.title(experiment)
    plt.legend()
    plt.show()

