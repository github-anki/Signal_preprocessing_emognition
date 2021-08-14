import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.signal import find_peaks
from .basic import normalize



def plot_signal_in_time(signal, frequency, title = 'Signal in time'):
    time = np.arange(0, (len(signal)/frequency), 1/frequency) / 60
    time = time[:len(signal)]
    fig = go.Figure()
    for col in signal:
        fig.add_trace(go.Scatter(
        x=time,
        y=signal[col],
        mode='lines',
        name=col
        ))
    fig.update_layout(title=title) 
    fig.update_xaxes(title='Time[min]')
    fig.update_yaxes(title='Signal')
    fig.show()
    

def plot_preprocessed_signal_in_time(signal, distance, height, title = 'Signal in time'):
    peaks, _ = find_peaks(signal, distance=distance, height=height)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        y=signal,
        mode='lines',
        name='Signal'
        ))
    fig.add_trace(go.Scatter(
        x=peaks,
        y=[signal[j] for j in peaks],
        mode='markers',
        marker=dict(
            size=8,
            color='red',
            symbol='cross'
        ),
        name='Detected Peaks'
    ))
    fig.update_layout(title=title) 
    fig.update_xaxes(title='Id')
    fig.update_yaxes(title='Signal')
    fig.show()


def plot_experiment(signal, experiment):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        y=signal.loc[signal['experiments'] == experiment, 'value'],
        mode='lines'
        ))
    fig.update_layout(title=experiment)
    fig.update_xaxes(title='Id')
    fig.update_yaxes(title='Signal')
    fig.show()

def plot_norm_experiment(signal_polar, signal_empatica, signal_samsung, experiment, frequency_polar, frequency_empatica, frequency_samsung):
    fig = go.Figure()
    signal_polar = signal_polar.loc[signal_polar['experiments'] == experiment, 'value']
    signal_polar = normalize(signal_polar)
    time_polar = np.arange(0, (len(signal_polar)/frequency_polar), 1/frequency_polar) / 60
    fig.add_trace(go.Scatter(
        x=time_polar[:len(signal_polar)],
        y=signal_polar,
        mode='lines',
        name='Polar'
        ))
    
    signal_empatica = signal_empatica.loc[signal_empatica['experiments'] == experiment, 'value']
    signal_empatica = normalize(signal_empatica)
    time_empatica = np.arange(0, (len(signal_empatica)/frequency_empatica), 1/frequency_empatica) / 60
    
    fig.add_trace(go.Scatter(
        x=time_empatica[:len(signal_empatica)],
        y=signal_empatica,
        mode='lines',
        name='Empatica'
        ))
    
    signal_samsung = signal_samsung.loc[signal_samsung['experiments'] == experiment, 'value']
    signal_samsung = normalize(signal_samsung)
    time_samsung = np.arange(0, (len(signal_samsung)/frequency_samsung), 1/frequency_samsung) / 60
    fig.add_trace(go.Scatter(
        x=time_samsung[:len(signal_samsung)],
        y=signal_samsung,
        mode='lines',
        name='Samsung'
        ))
    fig.update_layout(title=experiment)
    fig.update_xaxes(title='Time[min]')
    fig.update_yaxes(title='Signal')
    fig.show()
