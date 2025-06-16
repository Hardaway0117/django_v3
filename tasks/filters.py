from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):
    # 自訂欄位：模糊搜尋 title
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    status = filters.CharFilter(field_name='status', lookup_expr='icontains')

    # 精確篩選是否完成
    is_completed = filters.BooleanFilter(field_name='is_completed')

    # 日期範圍搜尋
    start_date = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Task
        fields = {
            'status': ['exact', 'icontains'],   # exact=精確,icontains=模糊搜尋
            'priority': ['exact', 'lt', 'gt'],
            'title': ['icontains'],
            'is_completed': ['exact'],
            'created_at': ['gte', 'lte'],
        }
