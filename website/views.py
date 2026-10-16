
import logging

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

logger = logging.getLogger(__name__)


def home(request):
    return render(request, "index.html")


def signin(request):
    return render(request, "signin.html")


@require_POST
def demo_submit(request):
    email = request.POST.get("email", "").strip()
    password = request.POST.get("password", "").strip()

    if not email:
        logger.warning("SIGN-IN : submission received without an email.")
        return JsonResponse({
            "ok": False,
            "message": "Please enter your email."
        }, status=400)

    # Demo only: do not log or store the submitted email or password.
    logger.info("SIGN-IN : email submission received successfully.")

    return JsonResponse({
        "ok": True,
        "message": " submission received successfully."
    })
