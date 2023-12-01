from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Module, Mentorship, Product, User, Comment
from django.contrib import messages
from .forms import ProductForm, CommentForm, DeleteCommentForm
from django.views import View
from django.http import Http404

@login_required
def home(request):
    return render(request, "core/home.html")


def view_modules(request):
    modules = Module.objects.all()
    return render(request, "core/modules.html", {"modules": modules})


def mentorship_forum(request):
    mentorships = Mentorship.objects.filter(mentor=request.user)
    return render(request, "core/mentorship_forum.html", {"mentorships": mentorships})


def request_mentorship(request, mentor_id):
    if request.method == 'POST':
        mentor = User.objects.get(id=mentor_id)
        Mentorship.objects.create(mentor=mentor, mentee=request.user)
        messages.success(request, 'Mentorship request sent successfully!')
        return redirect('mentorship_forum')
    return render(request, 'core/request_mentorship.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, "core/product_list.html", {"products": products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a view that displays the list of products
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def privacy_and_policy(request):
    return render(request, 'privacy_and_policy.html')

def services(request):
    return render(request, 'services.html')


def fashion_courses1(request):
    return render(request, 'fashion_courses1.html')

def fashion_courses2(request):
    return render(request, 'fashion_courses2.html')

def fashion_courses3(request):
    return render(request, 'fashion_courses3.html')

def wellness1(request):
    return render(request, 'wellness1.html')

def wellness2(request):
    return render(request, 'wellness2.html')

def fashion_courses(request):
    return render(request, 'fashion_courses.html')

def trends(request):
    return render(request, 'trends.html')

class CommentView(View):
    template_name = 'comments/comments.html'
    

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        form = CommentForm()
        return render(request, self.template_name, {'comments': comments, 'form': form})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.save()
            return redirect('comments')
        comments = Comment.objects.all()
        return render(request, self.template_name, {'comments': comments, 'form': form})
    
    
class DeleteCommentView(View):
    template_name = 'comments/delete_comment.html'

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['comment_id'])
        delete_form = DeleteCommentForm()
        context = {'comment': comment, 'delete_form': delete_form}
        print(f"User: {request.user}")
        print(f"Comment owner: {comment.user}")
        print(f"User can delete: {comment.user_can_delete(request.user)}")
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['comment_id'])

        if 'delete_comment' in request.POST:
            delete_form = DeleteCommentForm(request.POST)
            if delete_form.is_valid():
                comment.delete()
                return redirect('home')

        delete_form = DeleteCommentForm()
        context = {'comment': comment, 'delete_form': delete_form}
        return render(request, self.template_name, context=context)