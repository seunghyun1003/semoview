from django.contrib import admin
from django.urls import path, include
from api import views #추가
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token #추가

urlpatterns = [
    path('admin/', admin.site.urls),
    #회원가입을 위한 url
    path('rest-auth/signup/', include('rest_auth.registration.urls')),
    #로그인/로그아웃을 위한 url
    path('rest-auth/', include('rest_auth.urls')),
    #로그인 토큰 받기 위한 url
    path('api-token-auth/obtain_token/', obtain_jwt_token),  # JWT 토큰 획득
    path('api-jwt-auth/refresh/', refresh_jwt_token), # JWT 토큰 갱신
    path('api-jwt-auth/verify/', verify_jwt_token),   # JWT 토큰 확인3
    
    path('ckeck/username', views.ckcekUsername, name='ckcekUsername'),

    path('', views.index, name='index'),
    path('stages', views.stagelist, name='stagelist'),
    path('reviews/<stage_pk>', views.thisStageReviewlist, name='thisStageReviewlist'),
    
    path('get/myreviews/userId/<user_Id>', views.MyReviewlist, name='MyReviewlist'),

    path('stage/<stage_pk>/create', views.thisStageReviewCreate, name='thisStageReviewCreate'),
    path('review/<review_pk>/delete', views.reviewDelete, name='reviewDelete'),
    path('get/review/<review_id>', views.getThisReview, name='getThisReview'),
    path('review/<review_pk>/update', views.reviewUpdate, name='reviewUpdate'),

    path('search/keyword/<keyword>', views.getSeachResult, name='getSeachResult'),
]


