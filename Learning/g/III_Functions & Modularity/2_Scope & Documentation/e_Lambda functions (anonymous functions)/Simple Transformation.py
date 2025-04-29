"""Create a list of numbers: nums = [10, 20, 30, 40, 50]
   Use map and a lambda function to create a new list where each number is increased by 5. """

def main() -> None:

    nums = [10, 20, 30, 40, 50]
    new_list = list(map(lambda x : x+5, nums))
    print(new_list)
    print(nums)
    # print(list(result))
    # Expected: [15, 25, 35, 45, 55]

if __name__ == "__main__":
    main()
