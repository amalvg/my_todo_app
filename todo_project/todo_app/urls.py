from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('cbvtask',views.TaskListView.as_view(),name='cbvtask'),
    path('cbvdetail/<int:pk>',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>',views.TaskDeleteView.as_view(),name='cbvdelete'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
#
# urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings)