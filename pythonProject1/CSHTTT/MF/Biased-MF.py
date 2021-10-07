import numpy as np


class MF_bias():
    def __init__(self, D_Train, beta, K, lamda, iterations):
        """

        :param D_Train: user-item rating matrix
        :param K: number of talent dimensions
        :param beta: learning rate
        :param lamda: regularization parameter
        :param iterations: stopping condition
        """

        self.D_Train = D_Train
        self.num_users, self.num_items = D_Train.shape
        self.K = K
        self.beta = beta
        self.lamda = lamda
        self.iterations = iterations

    def train(self):
        # initialize user and item latent feature matrix
        self.W = np.random.normal(scale=1. / self.K, size=(self.num_users, self.K))
        self.H = np.random.normal(scale=1. / self.K, size=(self.num_items, self.K))

        # initiate the biases
        self.b_u = np.zeros(self.num_users)
        self.b_i = np.zeros(self.num_items)
        self.b = np.mean(self.D_Train[np.where(self.D_Train != 0)])

        # create a list of training samples
        self.samples = [
            (u, i, self.D_Train[u, i])
            for u in range(self.num_users)
            for i in range(self.num_items)
            if self.D_Train[u, i] > 0
        ]

        # Perform stochastic gradient descent for number interactions
        for i in range(self.iterations):
            np.random.shuffle(self.samples)
            self.sgd()

    def sgd(self):
        """
        Perform stochastic gradient descent
        """

        for u, i, r in self.samples:
            # compute prediction and error
            r_bar = self.b + self.b_u[u] + self.b_i[i] + self.W[u, :].dot(self.H[i, :].T)
            e = r - r_bar
            b = b + self.beta*e
            # update biases
            self.b_u[u] += self.beta * (e - self.lamda * self.b_u[u])
            self.b_i[i] += self.beta * (e - self.lamda * self.b_i[i])

            # Update user and item latent feature matrix
            self.W[u, :] += self.beta * (e * self.H[i, :] - self.lamda * self.W[u, :])
            self.H[i, :] += self.beta * (e * self.W[u, :] - self.lamda * self.H[i, :])

    def matrix_after_training(self):
        """
        Computer the full matrix using the resultant biases, W and H
        """
        return self.b + self.b_u[:, np.newaxis] + self.b_i[np.newaxis:, ] + self.W.dot(self.H.T)