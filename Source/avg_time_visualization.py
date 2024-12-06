import matplotlib.pyplot as plt

def plot_dummy_results(dummy_results):
    """
    Function to plot data given in dictionary form with each function on a separate line.
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
    plt.grid(True)
    plt.show()

# Example usage
dummy_results = {
    "Operation for matrices to match": {
        10: 0.01,
        20: 0.03,
        30: 0.06,
        40: 0.12,
    },
    "Spectra Equality": {
        10: 0.005,
        20: 0.016,
        30: 0.027,
        40: 0.043,
    },
    "Cokolwike": {
        10: 0.015,
        20: 0.316,
        30: 5.010,
        40: 10.043,
    }
}

plot_dummy_results(dummy_results)
