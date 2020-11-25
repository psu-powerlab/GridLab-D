The main purpose of this file is to test the capablilities of switch object to control loads. This file has two loads. Each of which operates under the following condition, **If A is ON, B is OFF.** The status property of switch objects is controlled by player objects (csv files).
**There are different ways to control loads in GridLAB-D, I chose this way for testing purposes. Other methods may be chosen in the future.**

Files in this folder:
- OnOffLoads.glm: Reference file.
- switch1.player: player object 1 reads from this file. (Change its contents and check the output)
- switch2.player: player object 2 reads from this file. (Change its contents and check the output)  
  
Another method to control loads is by using Scheduling property in GridLAB-D. Try the following file:
- test_complimentary_load.glm (Frank)
