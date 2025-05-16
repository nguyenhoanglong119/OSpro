# Step 3: Custom RL Environment for CPU Scheduling

## Overview

This module is part of an Operating Systems project focused on optimizing CPU scheduling policies using Machine Learning and Reinforcement Learning.

In Step 3, we design and implement a *custom RL environment* that simulates a simplified operating system scheduler. The environment follows the OpenAI Gym interface and allows an RL agent to interact with the system by making scheduling decisions.

## Environment Design

The environment simulates a number of concurrent processes. Each process is characterized by resource metrics such as CPU usage, memory usage, and priority. The agent receives a full snapshot of the system state (observations), selects an action (e.g., which process to prioritize), and receives a reward based on the performance impact of that decision.

### Key Elements:
- *Observation Space*: Captures system state including CPU, memory, and priority values per process.
- *Action Space*: Represents available scheduling actions (e.g., selecting a process to run).
- *Reward Function*: Encourages decisions that lead to high throughput, low memory usage, and fair prioritization.

## Objective

The goal is to provide an interactive environment where an RL agent can learn optimal CPU scheduling strategies through trial and error, with rewards guiding it toward better performance.

## Notes

The environment is designed to be lightweight and extendable.
It can be used directly for training agents in Step 4 using PPO or other RL algorithms.
Future extensions may include support for preemption, I/O wait simulation, or real-system integration.
