Step 3: Custom RL Environment for CPU Scheduling
🔍 Overview
This module is part of an Operating Systems course project focused on exploring CPU scheduling strategies using Reinforcement Learning (RL).
In Step 3, we design and implement a custom RL environment that simulates a simplified operating system process scheduler. The environment adheres to the OpenAI Gym interface and enables an RL agent to learn scheduling policies by interacting with dynamic system states.

⚙️ Environment Design
The environment simulates multiple concurrent processes. Each process is described by normalized system metrics:
CPU usage
Memory usage
Priority
I/O wait time
Context switches
Execution time remaining
The RL agent receives the full system state (as a flat vector), chooses an action (which process to schedule or to noop), and receives a reward based on how well that decision balances efficiency and fairness.

🔑 Key Elements
Observation Space:
A continuous vector of shape (num_processes × 7), capturing normalized metrics for each process.
Action Space:
A discrete space with num_processes + 1 actions, where each index selects a process to run or performs no operation (noop).

Reward Function:
Designed to encourage:
High throughput (low CPU usage)
Low memory pressure
Prioritizing important tasks
Reducing I/O wait
Minimizing unnecessary context switches
Fair treatment of long-waiting processes

🎯 Objective
The environment allows the agent to learn optimal CPU scheduling strategies via trial and error. It is suitable for:
Testing classic scheduling policies (e.g. Round-Robin, SRTF)
Training RL agents using algorithms like PPO, DQN, etc.
Analyzing trade-offs in performance vs. fairness
