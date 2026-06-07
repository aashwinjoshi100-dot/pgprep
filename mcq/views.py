from .models import Result
from django.shortcuts import render

def quiz(request):
    questions = [
        {
            "question": "Normal BP?",
            "options": ["120/80", "140/90", "100/60", "160/100"],
            "answer": "120/80"
        },
        {
            "question": "RBC lifespan?",
            "options": ["60 days", "90 days", "120 days", "150 days"],
            "answer": "120 days"
        }
    ]

    score = 0

    if request.method == "POST":
        for i, q in enumerate(questions):
            selected = request.POST.get(f"q{i}")

            if selected == q["answer"]:
                score += 1

        Result.objects.create(
            score=score,
            total=len(questions)
        )

        return render(request, "mcq/result.html", {
            "score": score,
            "total": len(questions)
        })

    return render(request, "mcq/quiz.html", {
        "questions": questions
    })
