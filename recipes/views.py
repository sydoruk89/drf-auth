from django.shortcuts import render
from rest_framework import generics
from .serializer import RecipeSerializer
from .models import Recipe
from .permissions import IsAuthorOrReadOnly


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
