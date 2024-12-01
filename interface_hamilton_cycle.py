import Solution_proporsals
import Solution_proporsals.DiracTheoremSolution
import Spectral_stuff.interface
import hamilton_paths
import hamilton_paths.adding_edges_stack
import backtracking_extension
def do_check_on_graph(graph, isDirected):
    print("------ Checks on Hamiltonian Cycle -------")
    print("Dirac Theorem")
    print(Solution_proporsals.DiracTheoremSolution.is_hamiltonian_by_dirac(graph,isDirected))
    print("Spectral Theorems - only for non - directed graphs")
    print(Spectral_stuff.interface.check_spectral_theorems(graph))
    print("Exact check using backtracking")
    print(Spectral_stuff.interface.is_hamiltonian_cycle(graph))
    print("------ Minimal extensions -------")
    print("Dirac Method")
    updated_matrix = Solution_proporsals.DiracTheoremSolution.add_minimal_edges_by_dirac(graph, isDirected)
    for row in updated_matrix:
        print(row)
    print("Spectral Theorem Solution")
    updated_matrix=Spectral_stuff.interface.spectral_extension(graph)
    if updated_matrix is not None:
        for row in updated_matrix:
            print(row)
    else:
        print("Spectral Solution couldnt be applied")
    print("Greedy edge adition method")
    updated_matrix = hamilton_paths.adding_edges_stack.hamiltonian_extension_matrix(graph)
    for row in updated_matrix:
        print(row)
    print("Exact solution")
    number , updated_matrix = backtracking_extension.find_minimum_edges_to_hamiltonian(graph)
    for row in updated_matrix:
        print(row)
    print("----- Number Of Hamilton cycles ----")

    
    
    


