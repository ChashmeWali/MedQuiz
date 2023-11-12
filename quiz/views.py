from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import Profile
from .models import Quiz, Category
from django.db.models import Q
from quiz.models import QuizSubmission
from django.contrib import messages
import random


# Create your views here.
@login_required(login_url='login')
def all_quiz_view(request):

    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)

    quizzes = Quiz.objects.order_by('-created_at')
    categories = Category.objects.all()

    context = {"user_profile": user_profile, "quizzes": quizzes, "categories": categories}
    return render(request, 'All-quiz.html', context)

@login_required(login_url='login')
def search_view(request, category):

    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)

    # search by search bar
    if 'q' in request.GET:
        q = request.GET.get('q')
        query = Q(title__icontains=q) | Q(description__icontains=q)
        quizzes = Quiz.objects.filter(query).order_by('-created_at')
    
    # search by category
    elif category and category.strip():  # Check if category is not empty or just whitespace
        quizzes = Quiz.objects.filter(category__name__icontains=category).order_by('-created_at')
    
    else:
        quizzes = Quiz.objects.order_by('-created_at')

    categories = Category.objects.all()

    context = {"user_profile": user_profile, "quizzes": quizzes, "categories": categories}
    return render(request, 'All-quiz.html', context)


def quiz_view(request, quiz_id):
    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)

    quiz = Quiz.objects.filter(id=quiz_id).first()

    # Get all questions for the quiz
    all_questions = list(quiz.question_set.all())

    # Randomly select 10 questions
    selected_questions = random.sample(all_questions, 10)

    total_questions = len(selected_questions)

    if request.method == "POST":
        # Get the score
        score = int(request.POST.get('score', 0))

        # Check if the user has already submitted the quiz
        if QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists():
            messages.success(request, f"This time you scored {score} out of {total_questions}")
            return redirect('quiz', quiz_id)

        # save the new quiz submission
        submission = QuizSubmission(user=request.user, quiz=quiz, score=score)
        submission.save()

        # show the result in message
        messages.success(request, f"Quiz Submitted Successfully. You got {score} out of {total_questions}")
        return redirect('quiz', quiz_id)

    if quiz is not None:
        correct_answers = [choice.text for question in selected_questions for choice in question.choice_set.all() if choice.is_correct]
        context = {
            "user_profile": user_profile,
            "quiz": quiz,
            "selected_questions": selected_questions,
            "correct_answers": correct_answers
        }
    else:
        return redirect('all_quiz')

    return render(request, 'The_Quizzes.html', context)




    if quiz != None:
        context = {"user_profile": user_profile, "quiz": quiz}
    else:
        return redirect('all_quiz')
    return render(request, 'The_Quizzes.html', context)

    context = {"user_profile": user_profile, "quizzes": quizzes, "categories": categories}
    return render(request, 'The_Quizzes.html', context)



