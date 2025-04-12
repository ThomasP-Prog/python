"""Write a function find_disjoint_subsets(target_set, list_of_candidate_sets) 
   that finds all subsets within list_of_candidate_sets which are completely disjoint
   (have no elements in common) with the target_set. The function should return a list containing copies of these disjoint candidate subsets.
"""





# The set you want to check against for disjointness
target_set = {"python", "sql", "cloud"}

# The list of candidate sets to check
list_of_candidate_sets = [
    {"java", "c++"},            # Disjoint with target
    {"sql", "aws"},             # NOT disjoint (contains 'sql')
    {"javascript", "html"},     # Disjoint with target
    {"python", "docker"},       # NOT disjoint (contains 'python')
    {"go", "rust"},             # Disjoint with target
    {"cloud", "azure", "gcp"},  # NOT disjoint (contains 'cloud')
    {"data analysis", "ml"}     # Disjoint with target
]

# Expected output for this data (order in the list might vary):
# [ {'java', 'c++'}, {'javascript', 'html'}, {'go', 'rust'}, {'data analysis', 'ml'} ] 