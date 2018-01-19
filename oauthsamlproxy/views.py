from oauth2_provider.models import AccessToken
from django.http import HttpResponse, HttpResponseRedirect
import json

def login(request):
    """
    This method was called as a login form by oauth2_provider (LOGIN_FORM)
    This view MUST be an apache authenticated location ! (which provide the correct header)

    If user is authenticated redirect to next (oauth2 authorized view)
    If not (config error) display error message
    """
    if request.user.is_authenticated:
        if request.GET.get('next'):
            return HttpResponseRedirect(request.GET.get('next'))
    return HttpResponse('Authentication failed, please contact admins.')


def me(request):
    """
    oauth2_provider doesn't provide informations about connected user
    This method was called as /me with token_id
    Return informations about token's user (json) 
    """
    tok = request.GET.get('access_token')
    data = {}
    if tok:
        data['mail'] = str(AccessToken.objects.get(token=tok).user)
        data['id'] = str(AccessToken.objects.get(token=tok).user)
    return HttpResponse(json.dumps(data), content_type="application/json")
