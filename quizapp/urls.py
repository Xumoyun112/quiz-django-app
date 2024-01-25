from django.urls import path

from  .views import question, quiz, result_list

urlpatterns = [
    path('', quiz, name='quiz'),
    path('quiz/<int:pk>/', question, name='question'),
    path('results/', result_list, name='results')

]