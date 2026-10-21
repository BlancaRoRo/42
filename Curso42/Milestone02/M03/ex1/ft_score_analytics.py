import sys
# para recorrer una lista de usa list[1:], desde el primer argumento
# hasta el final 1:
# Funcionalidad: Pasa el score de cada jugador como argumento y
# calcula estadísticas


if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    count: int = 0
    total: int = 0
    score: list[int] = []
    for i in sys.argv[1:]:
        try:
            score += [int(i)]
        except ValueError:
            print(f"Invalid parameter: '{i}'")
    try:
        total = len(score)
        if total == 0:
            raise ValueError(
                "python3 ft_score_analytics.py <score1> <score2> ...")
        print(f"Scores processed: {score}")
        print(f"Total players: {total}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {sum(score)/total}")
        print(f"High score: {max(score)}")
        print(f"Low score: {min(score)}")
        print(f"Score range: {max(score) - min(score)}")
    except ValueError as e:
        print(f"No scores provided. Usage: {e}")
