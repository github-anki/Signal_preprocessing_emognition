import glob
import pandas as pd

def read_multiple_csv(paths, **read_csv_kwargs):
    return pd.concat([pd.read_csv(path, **read_csv_kwargs) for path in paths])

def read_polar(filepath_ekg, filepath_acc):
    df_ekg = pd.read_csv(filepath_ekg, sep=';')[['value']]
    df_acc = pd.read_csv(filepath_acc, sep=';')[['x', 'y', 'z']]
    return df_ekg, df_acc
    

def read_empatica(filepath_ppg, filepath_acc):
    df_ppg = pd.read_csv(filepath_ppg, sep=',', skiprows=2, names=['value'])
    df_acc = pd.read_csv(filepath_acc, sep=',', skiprows=2, names=['x', 'y', 'z'])
    return df_ppg, df_acc
    

def read_samsung(files_dir):
    filepaths_acc = sorted(glob.glob(files_dir + 'A*.csv'))
    filepaths_ppg = sorted(glob.glob(files_dir + 'P*.csv'))

    df_acc = read_multiple_csv(filepaths_acc, sep='\t')[['x', 'y', 'z']]
    df_ppg = read_multiple_csv(filepaths_ppg, sep='\t').rename(columns={'light_intensity': 'value'})[['value']]
    
    df_acc = df_acc.replace(',', '.', regex=True).apply(pd.to_numeric)
    df_ppg = df_ppg.replace(',', '.', regex=True).apply(pd.to_numeric)
    return df_ppg, df_acc


if __name__ == '__main__':
    # Movement
    ## Polar
    df_ekg, df_acc = read_polar(
        'Data/00_raw_data/ruch/Polar/ekgpolarruch.csv', 
        'Data/00_raw_data/ruch/Polar/accpolarruch.csv'
    )
    df_acc.to_csv('Data/01_unified_data/ruch/polar_acc.csv', index=False)
    df_ekg.to_csv('Data/01_unified_data/ruch/polar_ekg.csv', index=False)

    ## Empatica
    df_ppg, df_acc = read_empatica(
        'Data/00_raw_data/ruch/Empatica/ppgempaticaruch.csv', 
        'Data/00_raw_data/ruch/Empatica/accempaticaruch.csv'
    )
    df_acc.to_csv('Data/01_unified_data/ruch/empatica_acc.csv', index=False)
    df_ppg.to_csv('Data/01_unified_data/ruch/empatica_ppg.csv', index=False)

    ## Samsung
    df_ppg, df_acc = read_samsung('Data/00_raw_data/ruch/Samsung/')
    df_acc.to_csv('Data/01_unified_data/ruch/samsung_acc.csv', index=False)
    df_ppg.to_csv('Data/01_unified_data/ruch/samsung_ppg.csv', index=False)

    # Standing
    ## Polar
    df_ekg, df_acc = read_polar(
        'Data/00_raw_data/siedzaco/Polar/ekgpolar.csv', 
        'Data/00_raw_data/siedzaco/Polar/accpolar.csv'
    )
    df_acc.to_csv('Data/01_unified_data/siedzaco/polar_acc.csv', index=False)
    df_ekg.to_csv('Data/01_unified_data/siedzaco/polar_ekg.csv', index=False)

    ## Empatica
    df_ppg, df_acc = read_empatica(
        'Data/00_raw_data/siedzaco/Empatica/ppgempatica.csv', 
        'Data/00_raw_data/siedzaco/Empatica/accempatica.csv'
    )
    df_acc.to_csv('Data/01_unified_data/siedzaco/empatica_acc.csv', index=False)
    df_ppg.to_csv('Data/01_unified_data/siedzaco/empatica_ppg.csv', index=False)

    ## Samsung
    df_ppg, df_acc = read_samsung('Data/00_raw_data/siedzaco/Samsung/')
    df_acc.to_csv('Data/01_unified_data/siedzaco/samsung_acc.csv', index=False)
    df_ppg.to_csv('Data/01_unified_data/siedzaco/samsung_ppg.csv', index=False)
