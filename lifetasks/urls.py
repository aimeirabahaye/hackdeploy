from django.urls import path
import django
from django.conf import settings


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'worker-profile/<int:profile_id>/', views.workerProfile, name='workerProfile'),
    path(r'show-task/<int:ID>/', views.showTask, name='showTask'),
    path(r'create-job/', views.createJob, name='createJob'),
    path(r'worker-home/', views.workerHome, name='workerHome'),
    path(r'worker-home/housekeeping', views.housekeeping, name='housekeeping'),
    path(r'worker-home/education', views.education, name='education'),
    path(r'worker-home/technology', views.technology, name='technology'),
    path(r'worker-home/animals', views.animals, name='animals'),
    path(r'worker-home/repairs', views.repairs, name='repairs'),
    path(r'worker-home/delivery', views.delivery, name='delivery'),
    path(r'worker-home/entertainment', views.entertainment, name='entertainment'),
    path(r'me-poster/', views.mePoster, name='mePoster'),
    path(r'inbox-poster/<int:posterID>', views.posterInbox, name="inboxPoster"),
    path(r'poster-home/', views.posterHome, name='posterHome'),
]
