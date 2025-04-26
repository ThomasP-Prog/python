"""Write a function find_disjoint_subsets(target_set, list_of_candidate_sets) 
   that finds all subsets within list_of_candidate_sets which are completely disjoint
   (have no elements in common) with the target_set. The function should return a list containing copies of these disjoint candidate subsets.
"""
def find_disjoint_subsets(target_set : set[str], list_of_candidate_sets : list[set[str]]) -> list[set[str]]:
    """Find disjoint candidate in a list"""
    if not list_of_candidate_sets:
        return list()
    
    disjoint_subsets = [subset for subset in list_of_candidate_sets if subset.isdisjoint(target_set)]
    return disjoint_subsets

def print_disjoint(disjoint_subsets : list[set[str]]) -> None:
    """Format disjointed subjects"""
    if not disjoint_subsets:
        print("No disjointed subset")
        return
    
    print("Disjointed subjects :")
    print("-"*20)
    for i, subset in enumerate(disjoint_subsets):
        print(f"Set {i}: {subset}") 

def main() -> None:
    """main function"""
    target_set = {"python", "sql", "cloud"}

    list_of_candidate_sets = [
        {"java", "c++"},
        {"sql", "aws"},
        {"javascript", "html"},
        {"python", "docker"},
        {"go", "rust"},
        {"cloud", "azure", "gcp"},
        {"data analysis", "ml"}
    ]
    disjoint_subsets = find_disjoint_subsets(target_set,list_of_candidate_sets)
    print_disjoint(disjoint_subsets)

if __name__ == "__main__":
    main()