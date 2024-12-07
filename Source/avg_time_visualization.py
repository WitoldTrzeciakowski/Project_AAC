import test_metric
import matplotlib.pyplot as plt

def group_results_by_threshold(results, threshold=1):
    """
    Groups results into two dictionaries based on the last value in each operation's data.
    
    Parameters:
        results (dict): A dictionary where keys are operation labels and values are dictionaries
                        with matrix sizes as keys and performance metrics as values.
        threshold (float): The threshold for grouping results based on the last value.
    
    Returns:
        tuple: Two dictionaries - one for operations with the last value > threshold, 
               and another for those with the last value <= threshold.
    """
    above_threshold = {}
    below_threshold = {}

    for operation, data in results.items():
        # Get the last value (largest matrix size)
        last_value = list(data.values())[-1]
        if last_value > threshold:
            above_threshold[operation] = data
        else:
            below_threshold[operation] = data

    return above_threshold, below_threshold


def plot_dummy_results(dummy_results):
    """
    Function to plot data given in dictionary form with each function on a separate line,
    using a logarithmic scale on the y-axis for better readability of varying magnitudes.
    """
    plt.figure(figsize=(10, 6))

    for label, data in dummy_results.items():
        x_values = list(data.keys())
        y_values = list(data.values())
        plt.plot(x_values, y_values, marker='o', label=label)
 
    plt.xlabel("Matrix Size")
    plt.ylabel("Time (seconds)")
    plt.title("Performance Metrics for Operations")
    plt.legend()
    plt.grid(True, which="both", linestyle='--', linewidth=0.5) 
    plt.show()


results = test_metric.test_computational_performance()
print(results)
above, below = group_results_by_threshold(results)
plot_dummy_results(above)
plot_dummy_results(below)

