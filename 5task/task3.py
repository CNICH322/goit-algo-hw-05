import sys
from collections import Counter
def parse_log_line(line: str) -> dict:
    parts = line.strip().split(maxsplit=3)

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

def load_logs(file_path: str) -> list:
        with open(file_path, "r", encoding="utf-8") as file:
            return [parse_log_line(line) for line in file]
    

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    return Counter(log["level"] for log in logs)


def display_log_counts(counts: dict):
    print("\nРівень логування| Кількість")
    print("------------------|----------")

    for level, count in counts.items():
        print(f"{level} {count}")


def main():

    file_path = sys.argv[1]

    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2]

        filtered_logs = filter_logs_by_level(logs, level)

        print(f"\nДеталі логів рівня {level.upper()}:")

        for log in filtered_logs:
            print(
                f"{log['date']} {log['time']} {log['level']} {log['message']}"
            )


if __name__ == "__main__":
    main()