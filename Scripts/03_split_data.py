import sys
sys.path.append(".")

import pandas as pd
import numpy as np

from constants import *
from utils.basic import calculate_index_ppg

def split(signal_acc, signal_ppg, id_start, id_stop, experiment_name):
    signal_acc.loc[id_start:id_stop, 'experiments'] = experiment_name

    id_start = calculate_index_ppg(id_start, signal_acc, signal_ppg)
    id_stop = calculate_index_ppg(id_stop, signal_acc, signal_ppg)
    signal_ppg.loc[id_start:id_stop, 'experiments'] = experiment_name
    return signal_ppg, signal_acc


if __name__ == '__main__':
    # Sitting
    df_polar_sit_acc = pd.read_csv('Data/02_presynch_data/siedzaco/polar_acc.csv')
    df_polar_sit_ekg = pd.read_csv('Data/01_unified_data/siedzaco/polar_ekg.csv')
    df_polar_sit_ekg['experiments'] = None
    df_polar_sit_acc['experiments'] = None
    df_polar_sit_ekg, df_polar_sit_acc = split(df_polar_sit_acc, df_polar_sit_ekg, ID_START_WO_MOVE_POLAR_ACC, ID_STOP_WO_MOVE_POLAR_ACC, 'without_move')
    df_polar_sit_ekg, df_polar_sit_acc = split(df_polar_sit_acc, df_polar_sit_ekg, ID_START_LIGHT_POLAR_ACC, ID_STOP_LIGHT_POLAR_ACC, 'light')
    df_polar_sit_ekg, df_polar_sit_acc = split(df_polar_sit_acc, df_polar_sit_ekg, ID_START_HAND_MOVE_POLAR_ACC, ID_STOP_HAND_MOVE_POLAR_ACC, 'hand_move')
    df_polar_sit_ekg, df_polar_sit_acc = split(df_polar_sit_acc, df_polar_sit_ekg, ID_START_BREATH_POLAR_ACC, ID_STOP_BREATH_POLAR_ACC, 'breath')
    df_polar_sit_ekg.to_csv(('Data/03_split_data/siedzaco/polar_ekg.csv'))
    df_polar_sit_acc.to_csv(('Data/03_split_data/siedzaco/polar_acc.csv'))

    df_empatica_sit_acc = pd.read_csv('Data/02_presynch_data/siedzaco/empatica_acc.csv')
    df_empatica_sit_ppg = pd.read_csv('Data/01_unified_data/siedzaco/empatica_ppg.csv')
    df_empatica_sit_ppg['experiments'] = None
    df_empatica_sit_acc['experiments'] = None
    df_empatica_sit_ppg, df_empatica_sit_acc = split(df_empatica_sit_acc, df_empatica_sit_ppg, ID_START_WO_MOVE_EMPATICA_ACC, ID_STOP_WO_MOVE_EMPATICA_ACC, 'without_move')
    df_empatica_sit_ppg, df_empatica_sit_acc = split(df_empatica_sit_acc, df_empatica_sit_ppg, ID_START_LIGHT_EMPATICA_ACC, ID_STOP_LIGHT_EMPATICA_ACC, 'light')
    df_empatica_sit_ppg, df_empatica_sit_acc = split(df_empatica_sit_acc, df_empatica_sit_ppg, ID_START_HAND_MOVE_EMPATICA_ACC, ID_STOP_HAND_MOVE_EMPATICA_ACC, 'hand_move')
    df_empatica_sit_ppg, df_empatica_sit_acc = split(df_empatica_sit_acc, df_empatica_sit_ppg, ID_START_BREATH_EMPATICA_ACC, ID_STOP_BREATH_EMPATICA_ACC, 'breath')
    df_empatica_sit_ppg.to_csv(('Data/03_split_data/siedzaco/empatica_ppg.csv'))
    df_empatica_sit_acc.to_csv(('Data/03_split_data/siedzaco/empatica_acc.csv'))

    df_samsung_sit_acc = pd.read_csv('Data/02_presynch_data/siedzaco/samsung_acc.csv')
    df_samsung_sit_ppg = pd.read_csv('Data/01_unified_data/siedzaco/samsung_ppg.csv')   
    df_samsung_sit_ppg['experiments'] = None
    df_samsung_sit_acc['experiments'] = None
    df_samsung_sit_ppg, df_samsung_sit_acc = split(df_samsung_sit_acc, df_samsung_sit_ppg, ID_START_WO_MOVE_SAMSUNG_ACC, ID_STOP_WO_MOVE_SAMSUNG_ACC, 'without_move')
    df_samsung_sit_ppg, df_samsung_sit_acc = split(df_samsung_sit_acc, df_samsung_sit_ppg, ID_START_LIGHT_SAMSUNG_ACC, ID_STOP_LIGHT_SAMSUNG_ACC, 'light')
    df_samsung_sit_ppg, df_samsung_sit_acc = split(df_samsung_sit_acc, df_samsung_sit_ppg, ID_START_HAND_MOVE_SAMSUNG_ACC, ID_STOP_HAND_MOVE_SAMSUNG_ACC, 'hand_move')
    df_samsung_sit_ppg, df_samsung_sit_acc = split(df_samsung_sit_acc, df_samsung_sit_ppg, ID_START_BREATH_SAMSUNG_ACC, ID_STOP_BREATH_SAMSUNG_ACC, 'breath')
    df_samsung_sit_ppg.to_csv(('Data/03_split_data/siedzaco/samsung_ppg.csv'))
    df_samsung_sit_acc.to_csv(('Data/03_split_data/siedzaco/samsung_acc.csv'))

    # Movement
    df_polar_move_acc = pd.read_csv('Data/02_presynch_data/ruch/polar_acc.csv')
    df_polar_move_ekg = pd.read_csv('Data/01_unified_data/ruch/polar_ekg.csv')
    df_polar_move_ekg['experiments'] = None
    df_polar_move_acc['experiments'] = None
    df_polar_move_ekg, df_polar_move_acc= split(df_polar_move_acc, df_polar_move_ekg, ID_START_WALK_POLAR_ACC, ID_STOP_WALK_POLAR_ACC, 'walking')
    df_polar_move_ekg, df_polar_move_acc = split(df_polar_move_acc, df_polar_move_ekg, ID_START_RUN_POLAR_ACC, ID_STOP_RUN_POLAR_ACC, 'running')
    df_polar_move_ekg.to_csv(('Data/03_split_data/ruch/polar_ppg.csv'))
    df_polar_move_acc.to_csv(('Data/03_split_data/ruch/polar_acc.csv'))

    df_empatica_move_acc = pd.read_csv('Data/02_presynch_data/ruch/empatica_acc.csv')
    df_empatica_move_ppg = pd.read_csv('Data/01_unified_data/ruch/empatica_ppg.csv')
    df_empatica_move_ppg['experiments'] = None
    df_empatica_move_acc['experiments'] = None
    df_empatica_move_ppg, df_empatica_move_acc = split(df_empatica_move_acc, df_empatica_move_ppg, ID_START_WALK_EMPATICA_ACC, ID_STOP_WALK_EMPATICA_ACC, 'walking')
    df_empatica_move_ppg, df_empatica_move_acc = split(df_empatica_move_acc, df_empatica_move_ppg, ID_START_RUN_EMPATICA_ACC, ID_STOP_RUN_EMPATICA_ACC, 'running')
    df_empatica_move_ppg.to_csv(('Data/03_split_data/ruch/empatica_ppg.csv'))
    df_empatica_move_acc.to_csv(('Data/03_split_data/ruch/empatica_acc.csv'))

    df_samsung_move_acc = pd.read_csv('Data/02_presynch_data/ruch/samsung_acc.csv')
    df_samsung_move_ppg = pd.read_csv('Data/01_unified_data/ruch/samsung_ppg.csv')
    df_samsung_move_ppg['experiments'] = None
    df_samsung_move_acc['experiments'] = None
    df_samsung_move_ppg, df_samsung_move_acc = split(df_samsung_move_acc, df_samsung_move_ppg, ID_START_WALK_SAMSUNG_ACC, ID_STOP_WALK_SAMSUNG_ACC, 'walking')
    df_samsung_move_ppg, df_samsung_move_acc = split(df_samsung_move_acc, df_samsung_move_ppg, ID_START_RUN_SAMSUNG_ACC, ID_STOP_RUN_SAMSUNG_ACC, 'running')
    df_samsung_move_ppg.to_csv(('Data/03_split_data/ruch/samsung_ppg.csv'))
    df_samsung_move_acc.to_csv(('Data/03_split_data/ruch/samsung_acc.csv'))



    