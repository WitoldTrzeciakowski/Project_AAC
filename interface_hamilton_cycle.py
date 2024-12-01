import Solution_proporsals
import Solution_proporsals.DiracTheoremSolution
import Spectral_stuff.interface
import hamilton_paths
import hamilton_paths.adding_edges_stack
import backtracking_extension
import hamilton_paths.heuristic_number_hamiltons
import hamilton_paths.list_hamiltons
def do_check_on_graph(graph, isDirected):


    print("------ Checks on Hamiltonian Cycle -------")
    print("Dirac Theorem")
    dirac = Solution_proporsals.DiracTheoremSolution.is_hamiltonian_by_dirac(graph,isDirected)
    print(dirac)
    print("Spectral Theorems - only for non - directed graphs")
    spectral = Spectral_stuff.interface.check_spectral_theorems(graph)
    print(spectral)
    print("Exact check using backtracking")
    backtrack = Spectral_stuff.interface.is_hamiltonian_cycle(graph)
    print(backtrack)



    print("------ Minimal extensions -------")
    if not (backtrack or spectral or dirac):
        print("Dirac Method")
        updated_matrix = Solution_proporsals.DiracTheoremSolution.add_minimal_edges_by_dirac(graph, isDirected)
        print("exact solution to number of cycles problem")
        print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(updated_matrix)))
        print("Approximate solution:")
        print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(updated_matrix))

        for row in updated_matrix:
            print(row)
        print("Spectral Theorem Solution")
        updated_matrix=Spectral_stuff.interface.spectral_extension(graph)



        if updated_matrix is not None:
            for row in updated_matrix:
                print(row)

            print("exact solution to number of cycles problem")
            print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(updated_matrix)))
            print("Approximate solution:")
            print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(updated_matrix))
        else:
            print("Spectral Solution couldnt be applied")



        print("Greedy edge adition method")
        updated_matrix = hamilton_paths.adding_edges_stack.hamiltonian_extension_matrix(graph)
        for row in updated_matrix:
            print(row)
        print("exact solution to number of cycles problem")
        print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(updated_matrix)))
        print("Approximate solution:")
        print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(updated_matrix))

        print("Exact solution")
        number , updated_matrix = backtracking_extension.find_minimum_edges_to_hamiltonian(graph)

        print("exact solution to number of cycles problem")
        print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(updated_matrix)))
        print("Approximate solution:")
        print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(updated_matrix))

        for row in updated_matrix:
            print(row)
    #if innitial graph is hamiltonian say how many paths
    if  (backtrack or spectral or dirac):
        print("----- Number Of Hamilton cycles ----")
        print("exact solution to number of cycles problem")
        print(len(hamilton_paths.list_hamiltons.find_all_longest_cycles(graph)))
        print("Approximate solution:")
        print(hamilton_paths.heuristic_number_hamiltons.approximate_hamiltonian_cycles(graph))





    
    
    


