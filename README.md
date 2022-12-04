# SMETO
--------------------------------------------------------------------------------
Stable Matching for Energy-Minimized Task Offloading in Cloud-Fog Networks
-----------------------------------------------------------------------------------
Problem Statement
------------------------------------------------
Processing massive data consumes lot of energy in cloud fog networks; hence it is
essential to minimize the total energy consumption of a cloud fog-network as
battery life of fog nodes is limited. For minimization of energy in cloud fog
networks, we have to take different combinations of helpers and task nodes into
consideration, which involves combinatorial optimization. Combinatorial
optimization is an NP hard problem but it reduces to polynomial time due to
SMETO.
Hence, the problem statement is to minimize the total energy consumption of
cloud-fog network and the assignment of subtasks from task node (TN) to suitable
fog nodes (FN) so that there is a reduction in computation complexity of network
and we are able to find a stable solution for many to one matching.



-----------------------------------------------------
Proposed Approach
----------------------------------------------
The assignment of subtasks from the task node (TN) to appropriate fog nodes is
one of the most important difficulties in order to reduce the overall energy
consumption of a cloud-fog network (FNs). In order to solve this issue, a many-toone matching is used in this study. As the indexes of the preference lists (PL) of TNs
and FNs, respectively, we first propose two notions, Service Efficiency (SE) and
Energy Efficiency (EE). Then, a stable matching technique for energy-minimized
task offloading (SMETO) is suggested.

In accordance with the network environment, HNs produce PLs in descending
sequence with SE. The TN k determines the EE of each helper after receiving the
HNs' proposal, then chooses qk helpers from its PL to reduce its energy
consumption. The terms SE and EE are defined as follows:

• Service Efficiency: the index of PLs in HNs, denoted as λ

• Energy Efficiency: the index of PLs in TNs, denoted as η

------------------------------------------------------------------------------
Implementation
---------------------------------------------------------------------
• Tool: - Jupyter notebooks

•Language: - Python



You can go to the master branch and simply get the smeto.ipynb file which contains the hard coded nature of the algorithm given in the paper.It is not the complete dynamic implementation of paper but it contains the static implementation which emulates the SMETO algorithm.You can simply download the file and run it on your system to see the results.

--------------------------------
Reference
--------------------------------
The algorithm used is conference paper from IEEE named SMETO: Stable Matching for Energy-Minimized
Task Offloading in Cloud-Fog Networks

Link:- https://ieeexplore.ieee.org/document/8891292
