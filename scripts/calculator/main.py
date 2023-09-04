from basic.multiply import calculate_multiply
from basic.div import calculate_div
from geometry.square import CalculateAreaOfSquare
from geometry.circle import CalculateAreaOfCircle
from conditions.contition import evaluate_condition

if __name__ == "__main__":
    print("Multiply: ", calculate_multiply(2, 3))
    print("Div: ", calculate_div(2, 3))
    area_square = CalculateAreaOfSquare(2)
    print("Area square: ", area_square.calculate())
    area_circle = CalculateAreaOfCircle(2)
    print("Area circle: ", area_circle.calculate())
    print("Is true: ", evaluate_condition("3 == 2"))
