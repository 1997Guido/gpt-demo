from django.shortcuts import render, get_object_or_404
from .models import QueryCategory
from .services import get_query_response

def query_view(request, category_id):
    query_category = get_object_or_404(QueryCategory, pk=category_id)
    user_query = request.GET.get('user_query', '')

    if user_query:
        assistant_response = get_query_response(query_category, user_query)
    else:
        assistant_response = ''

    return render(request, 'query_view.html', {
        'query_category': query_category,
        'user_query': user_query,
        'assistant_response': assistant_response
    })
