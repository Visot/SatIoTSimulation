# SatIoTSimulation (Network simulation for MO655A)

This simulations are based on [CosmicBeats](https://github.com/microsoft/CosmicBeats-Simulator) examples.
To run a sQimulation 
```
git clone https://github.com/microsoft/CosmicBeats-Simulator.git
```
First, we need to create the observations for this; you need to copy create_observations.py to the base directory of CosmicBeats repository. Then execute:
```bash 
python create_observations.py $n
```
This will create n observation per number of satellites (100,200, ... , 1000),

Second, we must change some files to extract from the simulator; we open the folder summarizer, and substitute the *summarizerdatalayer.py* file with the one in our script folder.
```bash
cd CosmicBeats-Simulator/src/analytics/summarizers
```


Finally, we build an Analyzer jupyter-notebook to read these data and compute the metrics using the Cosmic-Beats analytics scripts.

Our generated observations can be found in the *observation* folder, and the results folder contains the output analytics by the Cosmic-Beats.