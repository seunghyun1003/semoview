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

from .models import *

from django.shortcuts import render

from django.contrib.auth import get_user_model

def index(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST'])
def ckcekUsername(request):
    ckusername = ''
    for key in request.data.keys():
        ckusername = key
    user = get_user_model().objects.filter(username=ckusername)
    
    ckuser_list = []
    for u in user:
        ckuser_list.append({
            'username': u.username, 
        })

    if len(ckuser_list) == 0:
        return Response(True)
    else:
        return Response(False)


def stagelist(request):
    stages = StageData.objects.all()
    stage_list = []

    reviews = Review.objects.all()

    for stage in stages:
        thisStageReviews = reviews.filter(stage_id = stage.id)
        stage_list.append({
            'id': stage.id, 
            'stageTitle': stage.stageTitle, 
            'stageImglink': stage.stageImglink,
            'pointAvg' : getPointAvg(thisStageReviews),
            'reviewCount' : len(thisStageReviews),
        })
    return JsonResponse(stage_list, safe=False)

def getPointAvg(thisStageReviews):
    sum = 0
    count = len(thisStageReviews)

    if count != 0 :
        for review in thisStageReviews:
            sum += review.point
        avg = sum/count
        return "{:.1f}".format(avg)
    else:
        return 0

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
        review_list.insert(0, {
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
        myreview_list.insert(0, {
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

