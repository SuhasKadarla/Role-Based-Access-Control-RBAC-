from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate, logout
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
import logging
logger = logging.getLogger(__name__)





# Register view
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login view
'''@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])  # Allow access to anyone
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"error": "Email and password are required."}, status=400)

    user = authenticate(username=email, password=password)
    if user:
        login(request, user)
        return Response({"message": "Login successful!"}, status=200)
    else:
        return Response({"error": "Invalid email or password."}, status=403)'''

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"error": "Email and password are required."}, status=400)

    user = authenticate(username=email, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(tokens, status=200)
    else:
        return Response({"error": "Invalid credentials."}, status=401)

# Logout view
'''@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure user is authenticated
def logout_view(request):
    logout(request)
    return Response({"message": "Logout successful!"}, status=200)'''


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logger.info(f"Headers: {request.headers}")
    logger.info(f"Body: {request.data}")
    try:
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout successful!"}, status=205)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    

# Admin dashboard (only accessible to admins)
'''@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_dashboard(request):
    # Check if the user is authenticated and is an admin
    if request.user.is_authenticated:
        if request.user.is_staff:  # Check if the user is an admin
            return Response({"message": "Welcome, Admin!"})
        else:
            raise PermissionDenied("You do not have permission to access this resource.")
    else:
        return Response({"error": "Authentication required."}, status=401)'''

@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_dashboard(request):
    logger.info(f"Headers: {request.headers}")
    logger.info(f"Body: {request.data}")
    print("Authorization Header:", request.headers.get('Authorization'))
    if request.user.is_staff:
        return Response({"message": "Welcome, Admin!"})
    return Response({"error": "Permission denied"}, status=403)

