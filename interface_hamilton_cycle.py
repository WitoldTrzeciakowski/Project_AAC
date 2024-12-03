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

def do_check_on_graph(graph, isDirected):
    def print_graph_update(original, updated, label):
        print(f"--- {label} ---")
        print("Original Graph:")
        for row in original:
            print(row)
        print("\nUpdated Graph:")
        for row in updated:
            print(row)

    print("------ Checks on Hamiltonian Cycle -------")
    
    print("Dirac Theorem")
    dirac = Solution_proporsals.DiracTheoremSolution.is_hamiltonian_by_dirac(graph, isDirected)
    print(f"Dirac result: {dirac}")

    print("Spectral Theorems - only for non-directed graphs")
    spectral = Spectral_stuff.interface.check_spectral_theorems(graph)
    print(f"Spectral result: {spectral}")

    print("Exact check using backtracking")
    backtrack = Spectral_stuff.interface.is_hamiltonian_cycle(graph)
    print(f"Backtracking result: {backtrack}")

    print("------ Minimal Extensions -------")
    if not (backtrack or spectral or dirac):
        print("DFS approach")
        graph_copy = copy.deepcopy(graph)
        updated_matrix = UnionFind.find_minimal_extension_to_hamiltonian_cycle(graph_copy)
        print_graph_update(graph, updated_matrix, "DFS Approach")
        print("Exact solution to the number of cycles problem")
        print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(updated_matrix)))
        print("Approximate solution:")
        print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(updated_matrix))

        print("Dirac Method")
        graph_copy = copy.deepcopy(graph)
        updated_matrix = Solution_proporsals.DiracTheoremSolution.add_minimal_edges_by_dirac(graph_copy, isDirected)
        print_graph_update(graph, updated_matrix, "Dirac Method")
        print("Exact solution to the number of cycles problem")
        print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(updated_matrix)))
        print("Approximate solution:")
        print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(updated_matrix))

        print("Spectral Theorem Solution")
        if not isDirected:
            graph_copy = copy.deepcopy(graph)
            updated_matrix = Spectral_stuff.interface.spectral_extension(graph_copy)
            if updated_matrix is not None:
                print_graph_update(graph, updated_matrix, "Spectral Theorem Solution")
                print("Exact solution to the number of cycles problem")
                print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(updated_matrix)))
                print("Approximate solution:")
                print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(updated_matrix))
            else:
                print("Spectral Solution couldn't be applied")
        else:
            print("Spectral Theorem Solution is not applicable for directed graphs.")

        print("Greedy Edge Addition Method")
        graph_copy = copy.deepcopy(graph)
        updated_matrix = hamilton_paths.adding_edges_stack.hamiltonian_extension_matrix(graph_copy)
        print_graph_update(graph, updated_matrix, "Greedy Edge Addition Method")
        print("Exact solution to the number of cycles problem")
        print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(updated_matrix)))
        print("Approximate solution:")
        print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(updated_matrix))

        print("Exact Solution")
        graph_copy = copy.deepcopy(graph)
        number, updated_matrix = backtracking_extension.find_minimum_edges_to_hamiltonian(graph_copy)
        print(f"Number of edges added: {number}")
        print_graph_update(graph, updated_matrix, "Exact Solution for Minimal Edges")
        print("Exact solution to the number of cycles problem")
        print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(updated_matrix)))
        print("Approximate solution:")
        print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(updated_matrix))

    if backtrack or spectral or dirac:
        print("----- Number Of Hamilton Cycles -----")
        print("Exact solution to the number of cycles problem")
        print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(graph)))
        print("Approximate solution:")
        print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(graph))
