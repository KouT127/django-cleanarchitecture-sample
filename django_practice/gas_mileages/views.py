from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.base import View

from django_practice.gas_mileages.models import GasMileage


class IndexView(View):
    def get(self, request, *args, **kwargs):
        # ManyToMany: prefetch
        # OneToMany: related
        queryset = GasMileage.objects.all()#.select_related('users').select_related('motorcycles')
        # keyword = request.GET.get('keyword')
        # if keyword:
        # queryset = queryset.filter(
        #     Q(dser_id__icontains=1) | Q(description__icontains=1)
        # )
        context = {
            'mileage_list': queryset,
        }
        return render(request, 'gas_mileages/gas_mileage_list.html', context)

class CreateView(View):

    def get(self, request, *args, **kwargs):
        context ={
        }
        return render(request, 'gas_mileages/gas_mileage_list.html', context)

    def post(self, request, *args, **kwargs):
        pass

# class DeleteView(View):
#     model = GasMileage
#     success_url = reverse_lazy('gas_mileages:index')
#     def delete(self, request, *args, **kwargs):
#         result = super().delete(request, *args, **kwargs)
#         messages.success(
#             self.request, '「{}」を削除しました'.format(self.object))
#         return render(request, 'gas_mileages/gas_mileage_list.html', messages)

class DeleteView(DeleteView):
    model = GasMileage
    success_url = reverse_lazy('gas_mileages:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

index = IndexView.as_view()
delete = DeleteView.as_view()