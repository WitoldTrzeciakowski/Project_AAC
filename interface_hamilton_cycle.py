import Solution_proporsals
import Solution_proporsals.DiracTheoremSolution
import Spectral_stuff.interface
import hamilton_paths
import hamilton_paths.adding_edges_stack
import backtracking_extension
import hamilton_paths.heuristic_number_hamiltons
import hamilton_paths.list_hamiltons
import UnionFind
import copy
import maximum_cycle

def do_check_on_graph(graph, isDirected):
    def print_graph_update(original, updated, label):
        print(f"--- {label} ---")
        print("Original Graph(left) & Updated Graph(right)")
        max_rows = max(len(original), len(updated))
        for i in range(max_rows):
            row1 = original[i] if i < len(original) else " " * len(str(original[0]))
            row2 = updated[i] if i < len(updated) else " " * len(str(updated[0]))
            print(f"{row1}  |  {row2}")

    print("\n------ Checks on Hamiltonian Cycle -------")

    # Dirac's Theorem Check
    if input("Do you want to use Dirac Theorem approximation y/n? ") == "y":
        dirac = Solution_proporsals.DiracTheoremSolution.is_hamiltonian_by_dirac(graph, isDirected)
        print(f"Dirac Theorem results: {dirac}")

    # Spectral Theorems Check (only for undirected graphs)
    spectral = None
    if not isDirected and input("Do you want to use Spectral Theorems approximation y/n? ") == "y":
        spectral = Spectral_stuff.interface.check_spectral_theorems(graph)
        print(f"Spectral Theorems - only for non-directed graphs - result: {spectral}")

    # Exact Backtracking Check
    backtrack = None
    if input("Do you want to use Exact backtracking y/n? ") == "y":
        backtrack = Spectral_stuff.interface.is_hamiltonian_cycle(graph)
        print(f"Exact check using backtracking: {backtrack}")

    # Minimal Extensions if no solution is found
    if not (backtrack or spectral or dirac):
        print("\n------ Minimal Extensions -------")

        def count_hamiltonian_cycles(updated_matrix, label):
            if input(f"Do you want to calculate the number of Hamiltonian cycles for the {label} graph y/n? ") == "y":
                print(f"----- Number Of Hamiltonian Cycles ({label}) -----")
                if input("Do you want to use exact solution y/n? ") == "y":
                    print("Exact solution:", len(maximum_cycle.maximum_cycle_dfs_optimized(updated_matrix)))
                if input("Do you want to use approximate solution y/n? ") == "y":
                    print("Approximate solution:", maximum_cycle.longest_cycle_length(updated_matrix)[1])
                if input("Do you want to use Monte Carlo approximation y/n? ") == "y":
                    print("Monte Carlo approximation:", hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(updated_matrix))

        # DFS Extension
        if input("Do you want to use DFS Approach for minimal extensions y/n? ") == "y":
            graph_copy = copy.deepcopy(graph)
            updated_matrix = UnionFind.find_minimal_extension_to_hamiltonian_cycle(graph_copy)
            print_graph_update(graph, updated_matrix, "DFS Approach")
            count_hamiltonian_cycles(updated_matrix, "DFS Approach")

        # Dirac Method Extension
        if input("Do you want to use Dirac Method for minimal extensions y/n? ") == "y":
            graph_copy = copy.deepcopy(graph)
            updated_matrix = Solution_proporsals.DiracTheoremSolution.add_minimal_edges_by_dirac(graph_copy, isDirected)
            print_graph_update(graph, updated_matrix, "Dirac Method")
            count_hamiltonian_cycles(updated_matrix, "Dirac Method")

        # Spectral Theorem Extension
        if not isDirected and input("Do you want to use Spectral Theorem extension y/n? ") == "y":
            graph_copy = copy.deepcopy(graph)
            updated_matrix = Spectral_stuff.interface.spectral_extension(graph_copy)
            if updated_matrix is not None:
                print_graph_update(graph, updated_matrix, "Spectral Theorem Solution")
                count_hamiltonian_cycles(updated_matrix, "Spectral Theorem Solution")
            else:
                print("Spectral Solution couldn't be applied.")

        # Greedy Edge Addition Method
        if input("Do you want to use Greedy Edge Addition Method y/n? ") == "y":
            graph_copy = copy.deepcopy(graph)
            updated_matrix = hamilton_paths.adding_edges_stack.hamiltonian_extension_matrix(graph_copy)
            print_graph_update(graph, updated_matrix, "Greedy Edge Addition Method")
            count_hamiltonian_cycles(updated_matrix, "Greedy Edge Addition Method")

        # Exact Solution for Minimal Edges
        if input("Do you want to use Exact Solution for Minimal Edges y/n? ") == "y":
            graph_copy = copy.deepcopy(graph)
            number, updated_matrix = backtracking_extension.find_minimum_edges_to_hamiltonian(graph_copy)
            print(f"Number of edges added: {number}")
            print_graph_update(graph, updated_matrix, "Exact Solution for Minimal Edges")
            count_hamiltonian_cycles(updated_matrix, "Exact Solution for Minimal Edges")

    # Hamiltonian Cycles Counting for Original Graph
    if input("Do you want to calculate the number of Hamiltonian cycles in the original graph y/n? ") == "y":
        print("----- Number Of Hamiltonian Cycles (Original Graph) -----")
        if input("Do you want to use exact solution y/n? ") == "y":
            print("Exact solution to the number of cycles problem:", len(maximum_cycle.maximum_cycle_dfs_optimized(graph)))
        if input("Do you want to use approximate solution y/n? ") == "y":
            print("Approximate solution:", maximum_cycle.longest_cycle_length(graph)[1])
        if input("Do you want to use Monte Carlo approximation y/n? ") == "y":
            print("Monte Carlo approximation:", hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(graph))
