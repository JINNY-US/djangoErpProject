from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/erp')
    else:
        return redirect('/sign-in')


def erp(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            user = request.user
            return render(request, 'erp/test.html')


# def product_list(request):
#     # 등록 된 상품의 리스트를 볼 수 있는 view
#
# @login_required
# def product_create(request):
#     # 상품 등록 view