
import math

def compute_task(iterations, output):
    """
    Simulates a processor-heavy routine by performing repeated mathematical transformations.
    Each result is appended to the shared output list.
    """
    for number in range(iterations):
        transformed = math.pow(math.sqrt(number), 2)
        output.append(transformed)
