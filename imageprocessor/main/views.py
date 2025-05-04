from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageUploadForm
from .models import ProcessedImage
from .services.image_processor import ImageProcessor


def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            result = ImageProcessor.process_image(request.FILES['image'])
            return JsonResponse({'result': result['result']})

    form = ImageUploadForm()
    records = ProcessedImage.objects.all().order_by('-upload_time')
    return render(request, 'main/home.html', {'form': form, 'records': records})


@csrf_exempt
def process_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        result = ImageProcessor.process_image(request.FILES['image'])
        return JsonResponse({'result': result['result']})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def send_test_requests(request):
    if request.method == 'POST':
        for _ in range(100):
            ImageProcessor.process_image(request.FILES['image'])
        return redirect('home')
    return JsonResponse({'error': 'Invalid request'}, status=400)
