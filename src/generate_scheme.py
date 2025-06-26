import itertools
from typing import List, Tuple

def generate_schedule(
    num_teams: int,
    poule_sizes: Tuple[int, ...],
    max_fields: int,
    num_breaks: int
) -> List[List[Tuple[int, int, int]]]:
    """
    Generate a fair schedule (match schedule).
    Each match: (team1, team2, referee)
    Returns a list of rounds, each round is a list of matches.
    Each team can only have one role per round (playing or referee).
    """
    # Assign teams to poules
    teams = list(range(1, num_teams + 1))
    poules = []
    idx = 0
    for size in poule_sizes:
        poules.append(teams[idx:idx+size])
        idx += size

    # Generate all matches for each poule
    all_matches = []
    for poule in poules:
        poule_matches = []
        for i in range(len(poule)):
            for j in range(i+1, len(poule)):
                poule_matches.append((poule[i], poule[j]))
        all_matches.extend(poule_matches)

    rounds = []
    scheduled_matches = set()
    match_list = list(all_matches)
    while match_list:
        round_matches = []
        used_teams = set()
        # Schedule up to max_fields matches per round
        for match in match_list[:]:
            t1, t2 = match
            # Find a referee not playing this round
            possible_refs = [t for t in teams if t not in used_teams and t != t1 and t != t2]
            if t1 not in used_teams and t2 not in used_teams and possible_refs:
                referee = possible_refs[0]
                round_matches.append((t1, t2, referee))
                used_teams.update([t1, t2, referee])
                match_list.remove(match)
            if len(round_matches) >= max_fields:
                break
        if round_matches:
            rounds.append(round_matches)
        else:
            # If no matches could be scheduled, insert a break
            rounds.append([])
    # Insert breaks
    for _ in range(num_breaks):
        rounds.append([])
    return rounds

if __name__ == "__main__":
    # Example usage
    num_teams = 6
    poule_sizes = (4, 2)
    max_fields = 2
    num_breaks = 1
    schedule = generate_schedule(num_teams, poule_sizes, max_fields, num_breaks)
    for round_num, matches in enumerate(schedule, 1):
        print(f"Round {round_num}:")
        if matches:
            for m in matches:
                print(f"  Team {m[0]} vs Team {m[1]}, Referee: Team {m[2]}")
        else:
            print("  Break")

