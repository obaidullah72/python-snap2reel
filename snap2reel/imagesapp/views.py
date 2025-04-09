import os
from django.conf import settings
from django.shortcuts import render
from .forms import MusicUploadForm
from .utils import create_video_with_music
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def image_to_video_view(request):
    if request.method == 'POST':
        music_form = MusicUploadForm(request.POST, request.FILES)
        image_files = request.FILES.getlist('images')

        if music_form.is_valid() and image_files:
            fs = FileSystemStorage()
            image_paths = []

            for image in image_files:
                filename = fs.save(image.name, image)
                image_paths.append(os.path.join(settings.MEDIA_ROOT, filename))

            music_file = music_form.cleaned_data['music']
            music_path = fs.save(music_file.name, music_file)
            music_full_path = os.path.join(settings.MEDIA_ROOT, music_path)

            output_path = os.path.join(settings.MEDIA_ROOT, 'output_video.mp4')

            video_path = create_video_with_music(
                image_paths=image_paths,
                music_path=music_full_path,
                output_path=output_path
            )

            return render(request, 'imagesapp/video_result.html', {'video_url': fs.url('output_video.mp4')})

    else:
        music_form = MusicUploadForm()

    return render(request, 'imagesapp/upload.html', {
        'music_form': music_form
    })