def score_to_ects(score):
    if not isinstance(score, (int, float)):
        raise ValueError("Помилка: бал має бути числом")
    if score < 0 or score > 100:
        raise ValueError("Помилка: бал має бути від 0 до 100")
    
    if score >= 90:
        return 'A'
    elif score >= 82:
        return 'B'
    elif score >= 74:
        return 'C'
    elif score >= 64:
        return 'D'
    elif score >= 60:
        return 'E'
    else:
        return 'F'