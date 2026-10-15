from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST


def home(request):
    return render(request, "index.html")


def signin(request):
    return render(request, "signin.html")


@require_POST
def demo_submit(request):
    email = request.POST.get("email", "").strip()

    if not email:
        return JsonResponse({
            "ok": False,
            "message": "Please enter a demo email."
        }, status=400)

    # Demo only: never collect or save passwords.
    return JsonResponse({
        "ok": True,
        "message": "The demo request reached Django successfully."
    })
