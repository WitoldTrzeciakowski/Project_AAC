import test_speed_hamilton
import maximum_cycle

def test_maximum_cycle_performance():
    functions = {
        "Finding cycles with the use of DFS method": maximum_cycle.maximum_cycle_dfs_optimized,
        "Finding cycles with the use of matrix exponentiation approximation method": maximum_cycle.longest_cycle_length
    }
    test_speed_hamilton.test_computational_performance(functions, 3, 8)

if __name__ == "__main__":
    test_maximum_cycle_performance()