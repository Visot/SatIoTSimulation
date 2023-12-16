import json
import os
import numpy as np
import sys
import shutil
def create_observation(seed_value,n):
    data = json.load(open('configs/examples/config_1000iot.json'))
    # os valores estão ordenados 116: só iots
    temp = data.copy()
    val1 = data['topologies'][0]['nodes'][:116]
    val2 = data['topologies'][0]['nodes'][116:]
    val2 = np.random.RandomState(seed=seed_value).choice(val2,size=n,replace=False)
    temp['topologies'][0]['nodes'] = list(val1) + list(val2)
    root_directory = f'observations/{str(seed_value)}'
    if os.path.exists(os.path.join(os.getcwd(),'observations',str(seed_value))) == False:
        os.mkdir(root_directory)
    with open(os.path.join(root_directory,f'iot_{n}_config.json'), 'w') as f:    
        json.dump(temp, f)

if __name__ == '__main__':
    """
    This functions creates a group of observations n_observations
    using over the folder observations it will create a folder for each observations
    named as the random states.
    """
    obs = os.path.join(os.getcwd(),'observations')
    if os.path.exists(obs):
        print("... Removing olded observations files...")
        shutil.rmtree(obs)
        os.mkdir(obs)
        print("Files Removed")
    n_observations = int(sys.argv[1])
    randoms_seed = np.random.RandomState(seed=100).choice(range(0,1000),n_observations,replace=False)
    print(f"generated seed for each observations {randoms_seed}")
    for size in range(100,1001,100):
        for x in randoms_seed:
            create_observation(seed_value=x,n=size)
    print(f"created {n_observations} in folder Observations")
