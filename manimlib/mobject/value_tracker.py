<<<<<<< HEAD
import numpy as np

from manimlib.mobject.mobject import Mobject


class ValueTracker(Mobject):
    """
    Not meant to be displayed.  Instead the position encodes some
    number, often one which another animation or continual_animation
    uses for its update function, and by treating it as a mobject it can
    still be animated and manipulated just like anything else.
    """
    CONFIG = {
        "value_type": np.float64,
    }

    def __init__(self, value=0, **kwargs):
        super().__init__(**kwargs)
        self.set_value(value)

    def init_data(self):
        super().init_data()
        self.data["value"] = np.zeros((1, 1), dtype=self.value_type)

    def get_value(self):
        return self.data["value"][0, 0]

    def set_value(self, value):
        self.data["value"][0, 0] = value
        return self

    def increment_value(self, d_value):
        self.set_value(self.get_value() + d_value)


class ExponentialValueTracker(ValueTracker):
    """
    Operates just like ValueTracker, except it encodes the value as the
    exponential of a position coordinate, which changes how interpolation
    behaves
    """

    def get_value(self):
        return np.exp(ValueTracker.get_value(self))

    def set_value(self, value):
        return ValueTracker.set_value(self, np.log(value))


class ComplexValueTracker(ValueTracker):
    CONFIG = {
        "value_type": np.complex128
    }
=======
import numpy as np

from manimlib.mobject.mobject import Mobject
from manimlib.utils.iterables import listify


class ValueTracker(Mobject):
    """
    Not meant to be displayed.  Instead the position encodes some
    number, often one which another animation or continual_animation
    uses for its update function, and by treating it as a mobject it can
    still be animated and manipulated just like anything else.
    """
    CONFIG = {
        "value_type": np.float64,
    }

    def __init__(self, value=0, **kwargs):
        self.value = value
        super().__init__(**kwargs)

    def init_data(self):
        super().init_data()
        self.data["value"] = np.array(
            listify(self.value),
            ndmin=2,
            dtype=self.value_type,
        )

    def get_value(self):
        return self.data["value"][0, :]

    def set_value(self, value):
        self.data["value"][0, :] = value
        return self

    def increment_value(self, d_value):
        self.set_value(self.get_value() + d_value)


class ExponentialValueTracker(ValueTracker):
    """
    Operates just like ValueTracker, except it encodes the value as the
    exponential of a position coordinate, which changes how interpolation
    behaves
    """

    def get_value(self):
        return np.exp(ValueTracker.get_value(self))

    def set_value(self, value):
        return ValueTracker.set_value(self, np.log(value))


class ComplexValueTracker(ValueTracker):
    CONFIG = {
        "value_type": np.complex128
    }
>>>>>>> d50717a3fcd9979f9efdbd21a857746010c407ad
