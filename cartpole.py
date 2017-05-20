import gym
from TD.QLearningAgent import QLearningAgent
from gym import wrappers
import math

"""
Trains the cartpole-v0 environment from OpenAI's gym for a predefined number of episodes

Currently uses one-step tabular Q-Learning.
"""

def main(episodes):
	env = gym.make('CartPole-v0')
	env = wrappers.Monitor(env, '../tmp/cartpole-experiment', force=True)

	n_actions = env.action_space.n
	observation_min = env.observation_space.low
	observation_max = env.observation_space.high

	observation_min[3] = -1
	observation_max[3] = 1
	num_bins = (2,2,6,3)

	agent = QLearningAgent(env, n_actions, observation_min, observation_max, num_bins)

	maxReward = agent.train(episodes)
	print('Maximum reward obtained: ' + repr(maxReward))
	env.close()

if __name__ == "__main__":
	episodes = 800
	main(episodes)