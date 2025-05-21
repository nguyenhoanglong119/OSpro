env = CPUSchedulerEnv()
obs = env.reset()

for _ in range(10):
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    env.render()
    print("Reward:", reward, "| Info:", info)
    if done:
        break
