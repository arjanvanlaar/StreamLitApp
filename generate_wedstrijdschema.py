import itertools
from typing import List, Tuple

def generate_wedstrijdschema(
    num_teams: int,
    poule_sizes: Tuple[int, ...],
    max_fields: int,
    num_breaks: int
) -> List[List[Tuple[int, int, int]]]:
    """
    Generate a fair wedstrijdschema (match schedule).
    Each match: (team1, team2, referee)
    Returns a list of rounds, each round is a list of matches.
    """
    # Assign teams to poules
    teams = list(range(1, num_teams + 1))
    poules = []
    idx = 0
    for size in poule_sizes:
        poules.append(teams[idx:idx+size])
        idx += size

    rounds = []
    for poule in poules:
        # Generate round-robin for each poule
        poule_matches = []
        for i in range(len(poule)):
            for j in range(i+1, len(poule)):
                poule_matches.append((poule[i], poule[j]))
        # Assign referees (teams not playing in the match)
        for match in poule_matches:
            possible_refs = [t for t in poule if t not in match]
            referee = possible_refs[0] if possible_refs else -1
            rounds.append([(match[0], match[1], referee)])

    # Group matches into rounds with max_fields and add breaks
    grouped_rounds = []
    for i in range(0, len(rounds), max_fields):
        grouped_rounds.append(rounds[i:i+max_fields])
    # Insert breaks
    for _ in range(num_breaks):
        grouped_rounds.append([])  # Empty round = break
    return grouped_rounds

if __name__ == "__main__":
    # Example usage
    num_teams = 6
    poule_sizes = (3, 3)
    max_fields = 2
    num_breaks = 1
    schedule = generate_wedstrijdschema(num_teams, poule_sizes, max_fields, num_breaks)
    for round_num, matches in enumerate(schedule, 1):
        print(f"Round {round_num}:")
        if matches:
            for match in matches:
                for m in match:
                    print(f"  Team {m[0]} vs Team {m[1]}, Referee: Team {m[2]}")
        else:
            print("  Break")
