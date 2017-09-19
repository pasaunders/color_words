"""Allow users to post colored and enlarged words."""

from django.shortcuts import render, redirect


def rendering(request):
    """Render page with the right custom words."""
    # {word: value for (word, value) in request.session if word is not 'number'}
    # context = dict(request.session.items())
    context = {}
    context['words'] = {
        word: value for (word, value) in request.session.items() if word != 'number'
        }
    # import pdb; pdb.set_trace()
    return render(request, 'words/index.html', context)


def add(request):
    """Add custom word to the session."""
    if 'number' not in request.session:
        request.session['number'] = 0
    if request.method == "POST":
        request.session['number'] += 1
        if 'big' in request.POST:
            large = True
        else:
            large = False
        request.session['word{}'.format(request.session['number'])] = [
            request.POST['word'],
            request.POST['color'],
            large,
        ]
    return redirect('/')


def clear(request):
    """Clear session of words."""
    request.session.flush()
    return redirect('/')
