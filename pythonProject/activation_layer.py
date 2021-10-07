from .Neural import Layer

class ActivationLayer(Layer):
    def __init__ (self , input_shape, output_shape, activation_primary):
        """

        :param input_shape:
        :param output_shape:
        :param activation_primary:
        """
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.activation = activation
        self.activation_prime = activation_prime


