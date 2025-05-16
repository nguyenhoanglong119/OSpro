from stable_baselines3 import PPO

model = PPO("MlpPolicy", CPUSchedulerEnv(), verbose=1)
model.learn(total_timesteps=10000)
