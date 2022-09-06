from manim import *

# Run in terminal with: manim linearTransformation.py LinearTransformationScene -pql


class LinearTransformationScene(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )


    def construct(self):
        matrix = [[1, 1], [0, 1]] # Input (Choose different and test)
        self.apply_matrix(matrix)
        self.wait()

