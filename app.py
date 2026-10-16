import sys

TASKS = [
    ("주간 보고서 초안 작성", "HIGH", False),
    ("회의 자료 작성", "MID", False),
    ("책상 정리", "LOW", False),
    ("이메일 답장", "HIGH", True),
]

PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}


def sorted_tasks(tasks, include_done=False):
    shown = [task for task in tasks if include_done or not task[2]]
    return sorted(shown, key=lambda task: PRIORITY_ORDER[task[1]])


def main():
    include_done = "--all" in sys.argv[1:]
    for title, priority, done in sorted_tasks(TASKS, include_done):
        suffix = " (완료)" if done else ""
        print(f"{title}({priority}){suffix}")


if __name__ == "__main__":
    main()
