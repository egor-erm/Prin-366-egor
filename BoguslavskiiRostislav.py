from math import copysign


class LinearRegression:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        self.total_a_change = 0
        self.total_b_change = 0
        self.lessons_trained = 0

    def predict(self, x):
        return self.a * x + self.b

    def accumulateTraining(self, question, answer):
        # f(x) = ax + b
        # E = (v - f(q)) ^ 2
        predicted = self.predict(question)
        dEa = -2 * (answer - predicted) * question
        dEb = -2 * (answer - predicted)
        self.total_a_change -= dEa
        self.total_b_change -= dEb
        self.lessons_trained += 1

    def normalize(self):
        m = max(abs(self.total_a_change), abs(self.total_b_change))
        if m != 0:
            self.total_a_change /= m
            self.total_b_change /= m

    def applyTraining(self, learnRate):
        self.total_a_change /= self.lessons_trained
        self.total_b_change /= self.lessons_trained
        self.a += self.total_a_change * learnRate
        self.b += self.total_b_change * learnRate
        self.total_a_change = 0
        self.total_b_change = 0
        self.lessons_trained = 0

    def applyTrainingBySign(self, step):
        self.total_a_change /= self.lessons_trained
        self.total_b_change /= self.lessons_trained
        self.a += copysign(step, self.total_a_change)
        self.b += copysign(step, self.total_b_change)
        self.total_a_change = 0
        self.total_b_change = 0
        self.lessons_trained = 0

    def trainByArray(self, QnAPairs):
        for question, answer in QnAPairs:
            self.accumulateTraining(question, answer)

    def __str__(self):
        return "{" + f"f(x) = {self.a}x + {self.b}" + "}"
