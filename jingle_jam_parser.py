import csv


INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.csv"

games = []


def create_game(title: str, description: str, key: str) -> dict:
    return {"title": title, "description": description, "key": key}


with open(INPUT_FILE, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if i == 0:
            sub1 = "("
            sub2 = ")"

            idx1 = line.index(sub1)
            idx2 = line.index(sub2)

            total_games = int(line[idx1 + len(sub1) : idx2])
        if i == 1:
            lines = lines[2:]
        if line == "\n":
            games.append(
                create_game(
                    lines[0].strip(), lines[1].strip(), lines[2].split(":")[1].strip()
                )
            )
            lines = lines[4:]

assert len(games) == total_games

with open(OUTPUT_FILE, "w") as f:
    field_names = list(games[0].keys())
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(games)
