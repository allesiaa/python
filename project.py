def find_golf_rankings(str):  # Split the input string into lines
    lines = str.split("\n")
    # Initialize a dictionary to store the golfers' scores
    scores = {}
    # Parse the scores for each golfer
    for line in lines:
        name, score_str = line.split(":")
        scores[name] = sum(int(score) for score in score_str.split(","))
    # Sort the golfers by their scores in descending order
    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    # Extract the first, second, third, and last place golfers
    first_place = sorted_scores[0]
    second_place = sorted_scores[1]
    third_place = sorted_scores[2]
    last_place = sorted_scores[-1]
    # Build the output string
    output = f"FIRST PLACE: {first_place[0]}\n"
    output += f"SECOND PLACE: {second_place[0]}\n"
    output += f"THIRD PLACE: {third_place[0]}\n"
    output += f"LAST PLACE: {last_place[0]}"
    return output


def read_data():
    file = open("project.txt", "r")
    data = ""
    for i in range(10):
        if i == 9:
            data += file.readline().strip()
            continue
        data += file.readline().strip() + "\n"
    return data


print(find_golf_rankings(read_data()))