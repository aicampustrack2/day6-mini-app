# app.py 계획

## Context
AGENTS.md 기준: 할 일을 우선순위 순서로 보여 주는 Python 터미널 앱. 프로젝트 폴더에는 현재 AGENTS.md만 있고 app.py는 없음(새로 만들어야 함).

## 읽은 파일
- AGENTS.md (프로젝트 폴더의 유일한 파일)
- app.py, 테스트 파일: 없음

## 만들거나 수정할 파일
- 만들기: app.py (단일 파일, 표준 라이브러리만 사용)
- 수정: 없음 (AGENTS.md 포함 다른 파일은 건드리지 않음)

## 구현할 함수
- add_task(tasks, title, priority): 할 일 추가
- sort_tasks(tasks): 우선순위 순 정렬 (같으면 입력 순서 유지)
- show_tasks(tasks): 정렬된 목록을 번호와 함께 출력
- main(): 입력 루프 (추가 / 목록 보기 / 종료)
- `if __name__ == "__main__": main()`

## 실행할 확인 명령
- uv run python --version
- uv run app.py (샘플 3건을 우선순위 뒤섞어 입력해 정렬 출력 확인)
- (테스트를 추가하기로 하면) uv run python -m unittest

## 결정이 필요한 질문
1. 우선순위 표현: 숫자(1=높음) vs 높음/중간/낮음
2. 저장 방식: 메모리만 vs 파일(JSON) 저장
3. 기능 범위: 추가·목록만 vs 완료·삭제까지
4. uv 프로젝트 초기화(pyproject.toml) 필요 여부: 없으면 `uv run app.py`는 단일 스크립트로 동작하므로 불필요
5. 테스트 파일(test_app.py) 추가 여부 (AGENTS.md상 파일 추가는 요청 시에만)
