import torch
import random
import numpy as np
from collections import deque
from snakeGame import SnakeGameAI, Direction, Point

MAX_MEMORY = 100000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0
        self.memory = deque(maxlen=MAX_MEMORY)
        # TODO make training model

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass
    def train_short_memory(self, state, action, reward, next_state, done):
        pass
    def get_actiom(self, state):
        pass

def train():
    plot_scores = []
    plot_mean_scores = []
    total_scores = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True:
        state_old = agent.get_state(game)
        final_move = game.get_action(state_old)
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)


        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done) 

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()
            print('Game', agent.n_games, 'Score', score, 'Record: ', record)

            # TODO plot stuff


if __name__ == '__main__':
    train()
