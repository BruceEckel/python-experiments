import concurrent.futures
import math

def perform_operation(data):
    # Perform a computationally intensive operation
    result = 0
    for i in range(10**7):
        result += math.sqrt(i ** 3 + i ** 2 + i * data)
    return result

def main(data_list):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Map the perform_operation function to each data item in parallel
        results = executor.map(perform_operation, data_list)
    return list(results)

if __name__ == "__main__":
    print(main(range(32)))