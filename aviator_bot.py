
"""
Aviator Crash Signal Bot
Historical-data analysis and paper-trading signals.
No real-money betting or automatic betting.
"""

import csv
import os
from statistics import mean

DATA_FILE = "crash_history.csv"
TARGET = 2.0


def load_results():
    if not os.path.exists(DATA_FILE):
        return []

    results = []
    with open(DATA_FILE, newline="", encoding="utf-8") as file:
        for row in csv.reader(file):
            try:
                value = float(row[0].lower().replace("x", "").strip())
                if value > 0:
                    results.append(value)
            except (ValueError, IndexError):
                continue
    return results


def analyze(results):
    if not results:
        print("No historical data found yet.")
        return

    hits = sum(value >= TARGET for value in results)
    rate = hits / len(results) * 100

    print("\n--- Aviator History Report ---")
    print("Rounds analyzed:", len(results))
    print(f"Rounds at or above {TARGET}x: {hits}")
    print(f"Historical hit rate: {rate:.1f}%")
    print(f"Average multiplier: {mean(results):.2f}x")

    # This is a tracking rule, not a prediction.
    print("\nNEXT ROUND: WAIT")
    print("Past rounds cannot reliably predict the next result.")


def main():
    print("AVIATOR CRASH SIGNAL BOT")
    print("Analysis only — no real-money betting.")

    results = load_results()
    analyze(results)

    print("\nAdd verified historical multipliers to")
    print(DATA_FILE, "to analyze your dataset.")


if __name__ == "__main__":
    main()
