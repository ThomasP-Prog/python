"""Given a list of sets, where each inner set represents the skills of a job applicant
   (e.g., applicants_skills = [{"python", "sql"}, {"python", "java", "cloud"}, {"sql", "cloud"}, {"python"}]),
   write a function that finds all possible pairs of applicants whose combined skills
   (union of their individual skill sets) cover a required set of skills (passed as another argument, e.g., 
   required_skills = {"python", "sql", "cloud"}). The function should return a set of tuples, 
   where each tuple contains the indices of the pair of applicants meeting the requirement."""

def find_applicant_pair(applicants_skills : list[set[str]], required_skills : set[str]) -> set[tuple[int,int]]:
    """Return pairs of applicants with the required skills"""
    if not applicants_skills:
        return set()
    
    found_applicants = set()
    n = len(applicants_skills)

    for app1 in range(n):
        for app2 in range(app1+1,n):
            app1_skills = applicants_skills[app1]
            app2_skills = applicants_skills[app2]
            combined_skills = app1_skills|app2_skills
            if combined_skills.issuperset(required_skills):
                found_applicants.add((app1,app2))

    return found_applicants

def print_found_applicants(found_applicants : set[tuple[int,int]] ):
    """Print pairs of applicants"""
    if not found_applicants:
        return
    print("Matching applicants :")
    print("-"*20)
    for applicants in found_applicants:
        print(f"{applicants[0]} and {applicants[1]}")


def main() -> None:
    """main function"""
    applicants_skills = [{"python", "sql"}, {"python", "java", "cloud"}, {"sql", "cloud"}, {"python"}]
    required_skills = {"python", "sql", "cloud"}
    found_applicants = find_applicant_pair(applicants_skills,required_skills)
    print_found_applicants(found_applicants)

if __name__ == "__main__":
    main()