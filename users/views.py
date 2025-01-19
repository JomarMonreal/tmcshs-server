from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new user
            user = serializer.save()

            # Authenticate and log in the user
            user = authenticate(username=user.username,
                                password=request.data.get('password'))

            if user is not None:
                login(request, user)

                # Generate the JWT token
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
