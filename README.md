# vr_lunar_exploration

[![arXiv](https://img.shields.io/badge/arXiv-1234.56789-b31b1b.svg)](https://arxiv.org/abs/2410.17132)
[![Citation](https://img.shields.io/badge/Cite-This%20Work-orange)](#citation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Unity project and supplementary materials for the VR lunar exploration framework presented at IAC 2024.

![image](project-overview.png)

Authors:

- Giacomo Franchini [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0009-0009-5641-8346)
- Brenno Tuberga

Supervisor:

- Marcello Chiaberge [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0000-0002-1921-0126)

### Requirements

- Unity Editor version: `2021.3.26f1`;
- Blender version: `3.6.0`;
- Meta Quest 3 headset. To set it up, please follow the official guide on https://www.meta.com. 

### Launch the framework

First clone this repository:

```zsh
git clone https://github.com/PIC4SeR/vr_lunar_exploration.git
```

Then open the Unity Hub, add it as a project, and launch it.

At the first opening, you could encounter compilation errors of some ROS-related scripts. When Unity is asking to enter the safe mode, press `Ignore` and let the Editor open the project. Then, in the upper toolbar select `Robotics->ROS Settings` and switch the protocol to `ROS2`. The Editor will compile again the scripts and the errors should be removed. 

## Citation

If you use this work, please cite:

```
@misc{franchini2024advancinglunarexplorationvirtual,
    title={Advancing lunar exploration through virtual reality simulations: a framework for future human missions}, 
    author={Giacomo Franchini and Brenno Tuberga and Marcello Chiaberge},
    year={2024},
    eprint={2410.17132},
    archivePrefix={arXiv},
    primaryClass={astro-ph.IM},
    url={https://arxiv.org/abs/2410.17132}, 
}
```