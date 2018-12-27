# class PurchaseList(generics.ListAPIView):
#     serializer_class = PurchaseSerializer
#
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         username = self.kwargs['username']
#         return Purchase.objects.filter(purchaser__username=username)