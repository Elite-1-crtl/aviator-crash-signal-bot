"""
Aviator Signal Bot
Historical analysis and paper-trading only.
No guaranteed predictions or real-money betting.
"""

import csv
import os
from statistics import mean

DATA_FILE = "crash_history.csv"
TARGETS = (1.77, 2.12)
MIN_HISTORY = 30


def load_results():
    if not os.path.exists(DATA_FILE):
        return []

    results = []

    with open(DATA_FILE, newline="", encoding="utf-8") as file:
        for row in csv.reader(file):
            try:
                value = float(
                    row[0].lower().replace("x", "").strip()
                )
                if value > 0:
                    results.append(value)
            except (ValueError, IndexError):
                continue

    return results


def analyze(results):
    print("\n--- AVIATOR SIGNAL BOT ---")

    if not results:
        print("SIGNAL: WAIT")
        print("No historical results found.")
        print("Add verified multipliers to crash_history.csv.")
        return

    print("Rounds analyzed:", len(results))
    print(f"Average multiplier: {mean(results):.2f}x")

    for target in TARGETS:
        hits = sum(value >= target for value in results)
        rate = hits / len(results) * 100
        print(
            f"Historical rounds reaching {target:.2f}x: "
            f"{rate:.1f}% ({hits}/{len(results)})"
        )

    print("\n--- CURRENT SIGNAL ---")

    if len(results) < MIN_HISTORY:
        print("SKIP — not enough historical data.")
    else:
        print("WAIT — history alone cannot predict the next round.")

    print(f"Lower target to evaluate: {TARGETS[0]:.2f}x")
    print(f"Higher target to evaluate: {TARGETS[1]:.2f}x")
    print("\nThese targets are not guaranteed safe odds.")


def main():
    results = load_results()
    analyze(results)


if __name__ == "__main__":
    main()
