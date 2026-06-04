import statistics

def resopnse(scores: list[int]) -> dict[str, int]:
    return {
        "student_count": len(scores),
        "highest_score": max(scores),
        "average_score": round(statistics.mean(scores), 2)   
    }


print(resopnse(scores = [80, 95, 70, 60]))