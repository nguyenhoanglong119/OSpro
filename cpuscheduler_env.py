import gym
from gym import spaces
import numpy as np

class CPUSchedulerEnv(gym.Env):
    def __init__(self):
        super(CPUSchedulerEnv, self).__init__()

        # Giả sử có 5 tiến trình đang chạy
        self.num_processes = 5

        # Observation: [CPU usage, RAM usage, priority] của mỗi tiến trình (5 tiến trình x 3 đặc trưng)
        self.observation_space = spaces.Box(low=0, high=100, shape=(self.num_processes, 3), dtype=np.float32)

        # Action: chọn 1 tiến trình để cấp CPU (chỉ số từ 0 đến 4)
        self.action_space = spaces.Discrete(self.num_processes)

        # Khởi tạo trạng thái
        self.state = self._generate_state()

    def _generate_state(self):
        # Sinh ngẫu nhiên trạng thái mô phỏng: [CPU%, RAM%, priority]
        return np.random.rand(self.num_processes, 3) * np.array([100, 100, 10])  # priority từ 0 đến 10

    def step(self, action):
        done = False

        # Lấy tiến trình được chọn để cấp CPU
        selected_process = self.state[action]

        # Giả định reward là throughput trừ đi penalty cho RAM cao và priority thấp
        reward = 1.0 * (100 - selected_process[0])  # throughput
        reward -= 0.5 * selected_process[1]          # RAM penalty
        reward += 0.2 * selected_process[2]          # ưu tiên cao thì tốt hơn

        # Cập nhật trạng thái mới (ở đây mô phỏng ngẫu nhiên)
        self.state = self._generate_state()

        return self.state, reward, done, {}

    def reset(self):
        self.state = self._generate_state()
        return self.state

    def render(self, mode='human'):
        print(f"Current state: {self.state}")

env = CPUSchedulerEnv()
obs = env.reset()

for _ in range(10):
    action = env.action_space.sample()  # random action
    obs, reward, done, _ = env.step(action)
    print(f"Action: {action}, Reward: {reward}")
