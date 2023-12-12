from datetime import datetime
import pandas as pd

def tabularise_clean(builds):
    """
    This function tabularises then clean the entire data from the parameter:
    1. builds -> List of objects (builds)
    
    The process is as follows:
    1. Creating a pandas dataframe for all the information we want
    2. Changing Level, Life and ES to integer; Normalising DPS and changing DPS to integer
    3. Saves the dataframe as csv with the current time
    """
    current_time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    
    df = pd.DataFrame({
        'Level': [build.level for build in builds],
        'Class': [build.cls for build in builds],
        'Ascendancy': [build.asc for build in builds],
        'DPS': [build.dps for build in builds],
        'Skill': [build.skill for build in builds],
        'Keystone': [build.keystone for build in builds],
        'Life': [build.life for build in builds],
        'ES': [build.es for build in builds]
    })
        
    # Level to int
    df['Level'] = df['Level'].astype(int)
    
    # DPS
    # - Replace M with 000000
    # - Remove 'dot'
    # - Change to int
    df['DPS'] = df['DPS'].str.replace('M', '000000').str.replace('dot', '').astype(int)
    
    # Life & ES to int
    df['Life'] = df['Life'].astype(int)
    df['ES'] = df['ES'].astype(int)
    
    df.to_csv(f'./data/poeninja_{current_time}.csv', index=False)