from django.db.models import Sum
from django.shortcuts import render
from rest_framework import generics
from .models import Lesson, ViewingHistory
from .serializers import *
from itertools import chain


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        return Lesson.objects.all()


class LessonByProductView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(product_id=product_id)


class LessonAndHistoryByProductView(generics.ListAPIView):
    serializer_class = ViewingHistorySerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        viewing_history = ViewingHistory.objects.filter(lesson_id__product_id__user_id=user,
                                                        lesson_id__product_id=product_id)

        return viewing_history


class ProductStatisticsView(generics.ListAPIView):
    serializer_class = ProductStatisticsSerializer

    def get_queryset(self):
        user = self.request.user
        products = Product.objects.all()

        product_statistics = []

        for product in products:
            total_views = ViewingHistory.objects.filter(lesson_id__product_id=product.id, status=True).count()
            total_watch_time = \
                ViewingHistory.objects.filter(lesson_id__product_id=product.id, status=True).aggregate(Sum('time'))[
                    'time__sum']
            total_students = User.objects.count()

            product_data = {
                'product_id': product.id,
                'product_name': product.name,
                'total_views': total_views,
                'total_watch_time_seconds': total_watch_time,
                'total_students': total_students,
            }

            product_statistics.append(product_data)

        return product_statistics
