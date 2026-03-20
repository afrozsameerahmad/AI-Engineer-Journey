'''Question:
Create a score tracker to understand scope:
1) Global scope -> bonus points
2) Enclosing scope -> student total score
3) Local scope -> score of each session
4) Use nested function and nonlocal keyword
'''

BONUS_POINTS = 5


def update_bonus(points):
    """Update global bonus points."""
    global BONUS_POINTS
    BONUS_POINTS = points


def create_score_tracker(student_name):
    """Return nested functions to add score and show final report."""
    total_score = 0
    session_count = 0

    def add_session_score(score):
        nonlocal total_score, session_count
        session_count += 1
        total_score += score + BONUS_POINTS
        print(f"Session {session_count}: score={score}, bonus={BONUS_POINTS}")

    def show_report():
        print(f"\nStudent      : {student_name}")
        print(f"Sessions     : {session_count}")
        print(f"Final score  : {total_score}")

    return add_session_score, show_report


update_bonus(3)
add_score, final_report = create_score_tracker("Samee")

add_score(20)
add_score(25)
add_score(18)
final_report()
