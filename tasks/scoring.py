from datetime import date
import math

def calculate_priority_score(task):
    """
    Calculates a 'Smart Score' to prioritize tasks.
    Higher score = Higher priority.
    """
    if not task.due_date:
        # If no due date, treat it as due in 7 days for calculation purposes
        days_until_due = 7
    else:
        days_until_due = (task.due_date - date.today()).days

    # --- FACTOR 1: URGENCY ---
    # We use an exponential decay curve.
    # If a task is overdue (negative days), priority skyrockets.
    # If it's due today (0), it's very high.
    if days_until_due < 0:
        urgency_score = 100 + (abs(days_until_due) * 5) # Overdue penalty
    elif days_until_due == 0:
        urgency_score = 90
    else:
        # Decays as the due date gets further away
        urgency_score = 80 / math.log(days_until_due + 2)

    # --- FACTOR 2: IMPORTANCE ---
    # Linear multiplier. Importance is 1-5.
    # 5 * 10 = 50 pts max
    importance_score = task.importance * 10

    # --- FACTOR 3: EFFORT ---
    # We prefer "Quick Wins" (Low effort) slightly for momentum, 
    # but not enough to overshadow critical tasks.
    # Lower effort = Higher score bonus.
    # 5 (Hard) -> 0 bonus. 1 (Easy) -> 20 bonus.
    effort_bonus = (5 - task.effort) * 5

    total_score = urgency_score + importance_score + effort_bonus
    
    return round(total_score, 2)