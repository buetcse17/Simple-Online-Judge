from django.shortcuts import render, redirect
from django.http import Http404
from django.core.files.storage import FileSystemStorage

from user.models import is_loggedin
from OJ.utils import add_user_information
from user.models import handle_exists, get_user_id
from .models import add_message, get_messages_all, set_seen_true, get_messages_with
# Create your views here.


def messages(request):
    if is_loggedin(request=request):
        context = {}
        context['messages'] = get_messages_all(request.session['user_id'])

        context = add_user_information(request=request, context=context)
        return render(request, 'message/messages.html', context=context)
    else:
        return redirect('signin')


def conversation(request, handle):
    if is_loggedin(request=request):
        if handle_exists(handle=handle):
            context = {}
            if request.method == 'POST':
                sender_id = request.session['user_id']
                receiver_id = get_user_id(handle=handle)
                attachment_location = None
                if 'attachment' in request.FILES:
                    data = request.FILES['attachment']

                    fs = FileSystemStorage()
                    attachment_location = fs.save(name=data.name, content=data)

                text = request.POST['text']

                #print(text)

                add_message(sender_id=sender_id, receiver_id=receiver_id,
                            text=text, attachment_location=attachment_location)

            context['messages'] = get_messages_with(
                sender_id=request.session['user_id'], receiver_id=get_user_id(handle))

            notun_message = 0

            for x in context['messages']:
                if x[-1] == 0:
                    notun_message = 1

            if notun_message:
                set_seen_true(sender_id=get_user_id(handle=handle),
                              receiver_id=request.session['user_id'])
                context['messages'] = get_messages_with(
                    sender_id=request.session['user_id'], receiver_id=get_user_id(handle))

            context = add_user_information(request=request, context=context)
            return render(request, 'message/conversation.html', context=context)
        else:
            raise Http404('No such user')
    else:
        return redirect('signin')
