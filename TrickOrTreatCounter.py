
# Date of completion: 07-19-2023


# Brief explanation of the program: This program calculates the total
# number of candies collected from each house in each lane during Halloween
# trick or treat. It asks the user how many lanes were visited and then
# prompts for the number of candies collected in each house for each lane.
# Finally, it calculates and displays the total candies and average
# candies collected in each lane.

# Function to get valid integer input
def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Main program
def main():
    # Step 1: Ask the user how many lanes were visited for trick and treat
    num_lanes = get_valid_integer_input("Enter the number of lanes: ")

    # Initialize lane counter
    lane = 1

    # Outer loop for lanes
    while lane <= num_lanes:
        print(f"\nLane {lane}")
        total_candies = 0

        # Inner loop for houses (nested within the lanes loop)
        for house in range(1, 4):
            candies = get_valid_integer_input(f"Enter the number of candies{house}: ")
            total_candies += candies

        # Calculate the average candies for the lane
        average_candies = total_candies / 3

        # Display the total candies and average candies for the lane
        print(f"Total candies from this lane is {total_candies}")
        print(f"Average candies from this lane: {average_candies:.2f}")

        # Increment lane counter
        lane += 1


if __name__ == "__main__":
    main()
