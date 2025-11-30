import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from .models import Task
from .scoring import calculate_priority_score

@csrf_exempt
def task_list_create(request):
    """
    GET: List all tasks sorted by Smart Score.
    POST: Create a new task.
    """
    if request.method == 'GET':
        tasks = Task.objects.filter(is_completed=False)
        
        # Convert to list of dicts and append smart score
        task_data = []
        for t in tasks:
            score = calculate_priority_score(t)
            task_data.append({
                'id': t.id,
                'title': t.title,
                'importance': t.importance,
                'effort': t.effort,
                'due_date': t.due_date,
                'score': score
            })
        
        # SORTING MAGIC: Sort by score descending
        task_data.sort(key=lambda x: x['score'], reverse=True)
        
        return JsonResponse({'tasks': task_data}, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Validation / Edge Case handling
        if not data.get('title'):
            return JsonResponse({'error': 'Title is required'}, status=400)
            
        task = Task.objects.create(
            title=data['title'],
            importance=int(data.get('importance', 3)),
            effort=int(data.get('effort', 3)),
            due_date=parse_date(data.get('due_date')) if data.get('due_date') else None
        )
        return JsonResponse({'message': 'Task created', 'id': task.id}, status=201)

@csrf_exempt
def task_detail(request, task_id):
    """
    DELETE: Remove a task (mark complete or delete).
    """
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Task deleted'})
        
    return JsonResponse({'error': 'Method not allowed'}, status=405)