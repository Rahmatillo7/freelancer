from django.urls import path
from .views import ReviewList, FreelancerReviewListView, ReviewDetailView

urlpatterns = [
    path('create/', ReviewList.as_view(), name='review-create'),
    path('freelancer/<int:freelancer_id>/', FreelancerReviewListView.as_view(), name='freelancer-reviews'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]