from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def home(request):
    """Render the main page and handle contact form submissions.

    The contact form is present on the page (included in `base.html`). Submissions are
    saved to the database as ContactMessage instances and a success message is shown.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks — your message has been received. I'll get back to you soon.",
            )
            return redirect("home")
        else:
            messages.error(
                request, "Please correct the errors below and resubmit the form."
            )
    else:
        form = ContactForm()

    return render(request, "base.html", {"form": form})
