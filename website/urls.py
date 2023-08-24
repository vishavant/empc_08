from django.urls import path

from website import views

app_name = 'website'


urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('courses', views.display_courses, name="courses"),
    path('online-courses', views.online_courses, name="online-courses"),
    path('offline-courses', views.offline_courses, name="offline-courses"),
    # path('contact-us', views.contact_us, name='contact-us'),
    path('contact-us', views.ContactUs.as_view(), name='contact-us'),
    path('join-us', views.JoinUs.as_view(), name='join-us'),
    path('about-us', views.about_us, name='about-us'),
    path('course-detail', views.course_detail, name='course-detail'),
    path('thanks', views.ThankYou.as_view(), name='thanks'),
    path('starting-course', views.starting_course_view, name="starting-course"),
    path('know-course', views.know_course_detail_view, name="know-course"),
    path('achieve-course', views.achieve_course_detail_view, name="achieve-course"),
]