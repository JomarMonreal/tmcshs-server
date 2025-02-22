from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verify_token(request):
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return JsonResponse({"error": "Token is missing or invalid"},
                            status=401)

    token = auth_header.split(' ')[1]  # Extract token after 'Bearer '

    try:
        # Verify and decode token
        decoded_token = AccessToken(token)
        user_id = decoded_token['user_id']  # Extract user ID if needed
        user = User.objects.get(id=user_id)
        return JsonResponse({"message": "Token is valid", "user_id": user_id,
                             "is_staff": user.is_staff}, status=200)

    except Exception:
        return JsonResponse({"error": "Invalid or expired token"}, status=401)


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Authenticate and log in the user
            user = authenticate(username=user.username,
                                password=request.data.get('password'))

            if user is not None:
                login(request, user)

                # Generate JWT token
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response({
                    "message": "User registered and logged in successfully!",
                    "access_token": access_token,
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"error": "Authentication failed after registration"},
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  # Create the session or set a token

            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Send the token in the response
            return Response({
                "message": "Login successful!",
                "access_token": access_token,
            }, status=status.HTTP_200_OK)

        else:
            return Response({"error": "Invalid credentials"},
                            status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=200)
