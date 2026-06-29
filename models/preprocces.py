import pandas as pd 
FEATURE_COLUMNS = [
    "battery_power", "blue", "clock_speed", "dual_sim", "fc", "four_g",
    "int_memory", "m_dep", "mobile_wt", "n_cores", "pc", "px_height",
    "px_width", "ram", "sc_h", "sc_w", "talk_time", "three_g",
    "touch_screen", "wifi"
]

def prepare_input(raw_data, scaler):
    df = pd.DataFrame(raw_data)[FEATURE_COLUMNS]  # enforce order, drop extras
    return scaler.transform(df)