from django.urls import path
from . import views
urlpatterns=[
    path('',views.contentlistview,name='content-home'),
    #path('about-us/',views.about,name='about-page'),
    #path('contact-us/',views.contact,name='contact-page'),
    path('<int:pk>/',views.postdetail,name='content-detail'),
    path('create/',views.ContentCreateView,name='content-create'),
    path('<int:pk>/update/',views.ContentUpdateView.as_view(),name='content-update'),
    path('<int:pk>/delete/',views.ContentDeleteView.as_view(),name='content-delete'),
    path('<str:username>/',views.UserPostListView.as_view(),name='user-post'),
    path('comment/<int:pk>/cdelete/',views.CommentDeleteView.as_view(),name='comment-delete'),
    path('<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    #path('post/test/<int:id>/',views.contentlistview,name='post-detail'),
]

#post_confirm_delete.html