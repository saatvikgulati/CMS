from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Content,Comment 
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import CommentForm,ContentCreateForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
'''class ContentListView(ListView): #default object name is object_list
    model=Content
    template_name='content/home.html'
    context_object_name='data'
    ordering=['-date_posted']
    paginate_by=2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Content.objects.filter(author=user)'''
class UserPostListView(ListView): #default object name is object_list
    model=Content
    template_name='content/home.html'
    context_object_name='data'
    #ordering=['-date_posted']
    paginate_by=2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Content.objects.filter(author=user).order_by('-date_posted')
class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Comment
    success_url='/content/'
    def test_func(self):
        comment=self.get_object()
        if self.request.user==comment.author:
            return True
        else:
            return False
    '''def get_success_url(self,**kwargs):
        return reverse('content-detail',kwargs={'pk':self.object.pk})'''

def contentlistview(request):
    data=Content.objects.all().order_by('-date_posted')
    context={
        'data':data
    }
    if request.method=='GET':
        query=request.GET.get('q')
        if query is not None:
            qs=Content.objects.all()
            qs1=qs.filter(title__icontains=query)
            qs2=qs.filter(body__icontains=query)
            qs3=qs.filter(summary__icontains=query)
            qs4=qs.filter(categories__icontains=query)
            final_qs=qs1|qs2|qs3|qs4
            context={
                'data':final_qs
            }
    return render(request,'content/home.html',context)
@login_required
def ContentCreateView(request):
    if request.method=='POST':
        form=ContentCreateForm(request.POST,request.FILES)
        user_id=request.user.id
        current_user=User.objects.filter(id=user_id).first()
        form.instance.author=current_user
        if form.is_valid():
            form.save()
            context={
                'object':Content.objects.filter(author=current_user).last()
            }
            return render(request,'content/content_detail2.html',context)
    else:
        form=ContentCreateForm()
    return render(request,'content/content_form.html',{'form':form})
'''class ContentCreateView(LoginRequiredMixin,CreateView):
    model=Content
    fields=['title','body','summary','categories','pdf']
    #template this class will look for is post_create
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)'''

class ContentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Content
    template_name='content/content_form.html'
    fields=['title','body','summary','categories','pdf']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
    def get_success_url(self,**kwargs):
        return reverse('content-detail',kwargs={'pk':self.object.pk})

class ContentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Content
    success_url='/content/' #not a var it is an underlining function
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
@login_required
def add_comment_to_post(request,pk,cform):
    pid=pk
    form=cform
    if request.method == 'POST':
        form=cform
        form.instance.author=request.user
        form.instance.post=Content.objects.filter(id=pid).first()
        if form.is_valid():
            form.save()
            context={
                'object':Content.objects.filter(id=pid).first(),
                'comments':Comment.objects.all(),
                'form':form
            }
            return render(request,'content/content_detail2.html',context)
    else:
        return render(request,'content/content_detail2.html',{'form':form})

def postdetail(request,pk):
    pid=pk
    cform=CommentForm()
    currentpost=Content.objects.filter(id=pid).first()
    context={
        'form':cform,
        'comments':Comment.objects.filter(post=currentpost),
        'object':Content.objects.filter(id=pid).first(),
    }
    if request.method == 'POST':
        cform=CommentForm(request.POST)
        add_comment_to_post(request,pid,cform)
    return render(request,'content/content_detail2.html',context)

'''def search(request):
    context={
        'data':Content.objects.all()
    }
    return render(request,'content/search.html',context)'''