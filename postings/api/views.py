from rest_framework import generics, mixins
from postings.models import BlogUser
from .serializer import BlogUserSerializer
from django.db.models import Q
from .permissions import IsOwnerOrReadOnly


# creation
class BlogUserAPIView(generics.CreateAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = BlogUserSerializer # represent la convertion en JSON
    permission_clases = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return BlogUser.objects.all()

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)    


# afficher tout les utilisateurs
class BlogUserListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = BlogUserSerializer # represent la convertion en JSON
    # faire des rechercher d l'articl en fonctio du titre et du contenu
    def get_queryset(self):
        qs= BlogUser.objects.all()
        query=self.request.GET.get("q")
        if query is not None:
            qs= qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
            return qs
        return BlogUser.objects.all()
    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)   
    # ajouter post
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  
        

#recuperation, mise à jour et suppression
class BlogUserRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = BlogUserSerializer # represent la convertion en JSON

    def get_queryset(self):
        return BlogUser.objects.all()



