from django.shortcuts import render
import json
from .models import PredictAgent,Issue
from django.http import JsonResponse

# Create your views here.
def agent_solution(request,id):
	predict_agent=PredictAgent.objects.filter(pk=id).exists()
	if predict_agent:
		predict_agent=PredictAgent.objects.filter(pk=id).values('agent','start_time','abandoned','abandoned_time','answer_time','resolved','resolved_time')
		status = 200
		return JsonResponse({'status':status,'data':list(predict_agent)},content_type='application/json')
	else:
		status=400
		return JsonResponse({'status':status,'agent':list(predict_agent)},content_type='application/json')