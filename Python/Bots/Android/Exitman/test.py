import os, gym, pyautogui

os.system("cls")
env = gym.make('CartPole-v1', render_mode="human")

# for i_episode in range(1): #how many episodes you want to run
#     observation = env.reset() #reset() returns initial observation

# for t in range(100):
#     env.render()
#     print(str(observation).split("[")[1].split("]")[0].replace(",", ""))
#     action = env.action_space.sample()
#     observation, reward, terminated, truncated, info = env.step(action)
#     if terminated:
#         print("Episode finished after {} timesteps".format(t+1))
#         break

# print(env.action_space)
# print(env.observation_space)
# print(env.observation_space.high)
# print(env.observation_space.low)
