from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserSerializer, ReviewSerializer

from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser 

import json

from .models import StageData
from .models import Review

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def stagelist(request):
    stages = StageData.objects.all()
    stage_list = []

    for stage in stages:
        stage_list.append({
            'id': stage.id, 
            'stageTitle': stage.stageTitle, 
            'stageImglink': stage.stageImglink
        })
    return JsonResponse(stage_list, safe=False)

def getThisReview(request, review_id):
    review = Review.objects.get(pk = review_id)
    reviewdata = []

    reviewdata.append({
        'id': review.id, 
        'stage_id': review.stage_id.id, 
        'user_id': review.user_id.id, 
        'reviewContents': review.reviewContents, 
        'point': review.point, 
        'created_at': review.created_at, 
        'updated_at': review.updated_at
    })
    return JsonResponse(reviewdata, safe=False)

def thisStageReviewlist(request, stage_pk):
    stages = StageData.objects.get(pk = stage_pk)
    reviews = Review.objects.all()
    thisStageReviews = reviews.filter(stage_id = stages.id)
    review_list = []
    for review in thisStageReviews:
        review_list.append({
            'id': review.id, 
            'stage_id': review.stage_id.id, 
            'user_id': review.user_id.id, 
            'user_username': review.user_id.username, 
            'reviewContents': review.reviewContents, 
            'point': review.point, 
            'created_at': review.created_at, 
            'updated_at': review.updated_at})
    return JsonResponse(review_list, safe=False)

def getSeachResult(request, keyword):
    stages = StageData.objects.all()
    searchedStages = stages.filter(stageTitle__contains=keyword)
    searched_stages_list = []
    for stage in searchedStages:
        searched_stages_list.append({
            'id': stage.id, 
            'stageTitle': stage.stageTitle, 
            'stageImglink': stage.stageImglink
        })
    return JsonResponse(searched_stages_list, safe=False)


@api_view(['GET', 'POST'])
@authentication_classes((JSONWebTokenAuthentication,))
def thisStageReviewCreate(request, stage_pk):
    if request.method == 'POST' :
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET' :
        stages = StageData.objects.get(pk = stage_pk)
        reviews = Review.objects.all()
        thisStageReviews = reviews.filter(stage_id = stages.id)
        serializer = ReviewSerializer(thisStageReviews,many=True)
        return Response(serializer.data)
        
    return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((JSONWebTokenAuthentication,))
def reviewUpdate(request, review_pk):
    review = Review.objects.get(pk = review_pk)

    if request.method == 'PUT' :
        review_data = JSONParser().parse(request) 
        serializer = ReviewSerializer(review, data=review_data)
        if serializer.is_valid():
            serializer.save() 
            return Response(review_data, status=status.HTTP_201_CREATED)
    else:
        review = Review.objects.get(pk = review_pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
        
    return Response(serializer.errors)

@api_view(['PUT', 'DELETE'])
def reviewDelete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response({ 'id': review_pk })


def MyReviewlist(request, user_Id):
    reviews = Review.objects.all()
    stages = StageData.objects.all()
    myReviews = reviews.filter(user_id = user_Id)
    myreview_list = []

    for myReview in myReviews:
        myreview_list.append({
            'id': myReview.id, 
            'stage_id': myReview.stage_id.id, 
            'stage_stageTitle' : stages[myReview.stage_id.id-1].stageTitle,
            'user_id': myReview.user_id.id, 
            'user_username': myReview.user_id.username, 
            'reviewContents': myReview.reviewContents, 
            'point': myReview.point, 
            'created_at': myReview.created_at, 
            'updated_at': myReview.updated_at})
    return JsonResponse(myreview_list, safe=False)

@api_view(['POST'])
@permission_classes([AllowAny, ]) #모든 사용자 접근가능
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password1 = request.data.get('password')
    password2 = request.data.get('password2')
		
	#1-2. 패스워드 일치 여부 체크
    if password1 != password2:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

