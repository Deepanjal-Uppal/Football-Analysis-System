from django.shortcuts import render, redirect
from .form import VideoUploadForm
from .models import VideoUpload
from football_analysis_main.main import main  # Adjust the import to your actual path
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def upload_video(request):
    video_url = None  # Initialize video_url variable

    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        video = request.FILES['video']
        # title = request.POST['title']
        
        if form.is_valid():
            # Save the uploaded video and store its URL
            video_instance = form.save()
            video_url = video_instance.video.url  # Get the URL of the uploaded video

            # Call the main function from your football analysis code
            input_video_path = video_instance.video.path  # Get the full path of the uploaded video
            output_video_path = 'output_videos/output_video.avi'  # Specify the output path

            # Run the football analysis
            main(input_video_path, output_video_path)  # Adjust this function call to your needs

            # Construct the correct URL (use + for URLs, don't use os.path.join)
            processed_video_url = settings.MEDIA_URL + 'output_videos/output_video.avi'

            # Render the success page with the processed video URL
            return render(request, 'upload_success.html', {'video_url': processed_video_url})

    else:
        form = VideoUploadForm()

    return render(request, 'upload.html', {'form': form})
