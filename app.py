TASKS = [
    ("주간 보고서 초안 작성", "HIGH", False),
    ("회의 자료 작성", "MID", False),
    ("책상 정리", "LOW", False),
    ("이메일 답장", "HIGH", True),
]

PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}


def pending_sorted(tasks):
    pending = [task for task in tasks if not task[2]]
    return sorted(pending, key=lambda task: PRIORITY_ORDER[task[1]])


def main():
    for title, priority, _ in pending_sorted(TASKS):
        print(f"{title}({priority})")


if __name__ == "__main__":
    main()
