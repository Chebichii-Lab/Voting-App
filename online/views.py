from online.models import Choice, Poll
from online.forms import AddPollForm, SignupForm, UserProfileForm
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    polls = Poll.objects.all()
    return render(request,'index.html', {'polls':polls})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')    
def user_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html',{ "profile_form": profile_form})

@login_required(login_url='/accounts/login/')
def polls_list(request):
    all_polls = Poll.objects.all()
    search_term = ''
    if 'name' in request.GET:
        all_polls = all_polls.order_by('text')

    if 'date' in request.GET:
        all_polls = all_polls.order_by('pub_date')

    if 'vote' in request.GET:
        all_polls = all_polls.annotate(Count('vote')).order_by('vote__count')

    if 'search' in request.GET:
        search_term = request.GET['search']
        all_polls = all_polls.filter(text__icontains=search_term)

    paginator = Paginator(all_polls, 6)  # Show 6 contacts per page
    page = request.GET.get('page')
    polls = paginator.get_page(page)

    get_dict_copy = request.GET.copy()
    # params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    # print(params)
    context = {
        'polls': polls,
        # 'params': params,
        'search_term': search_term,
    }
    return render(request, 'poll_list.html', context)

@login_required()
def polls_add(request):
    # if request.user('polls.add_poll'):
        if request.method == 'POST':
            form = AddPollForm(request.POST)
            if form.is_valid:
                poll = form.save(commit=False)
                poll.owner = request.user
                poll.save()
                # new_choice1 = Choice(poll=poll, choice_text=form.cleaned_data['choice1']).save()
                # new_choice2 = Choice(poll=poll, choice_text=form.cleaned_data['choice2']).save()

                messages.success(
                    request, "Poll & Choices added successfully.", extra_tags='alert alert-success alert-dismissible fade show')

                return redirect('list')
        else:
            form = AddPollForm()
        context = {
            'form': form,
        }
        return render(request, 'add_poll.html', context)
    # else:
    #     return HttpResponse("Sorry but you don't have permission to do that!")
