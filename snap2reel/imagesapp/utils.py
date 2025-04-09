from moviepy import ImageSequenceClip, AudioFileClip
from PIL import Image
import os

def create_video_with_music(image_paths, music_path, output_path, max_audio_duration=30):
    target_size = (720, 480)  # Standard video size

    # Step 1: Resize all images to same size
    resized_images = []
    for path in image_paths:
        img = Image.open(path).convert("RGB")
        img = img.resize(target_size)
        temp_path = f"{path}_resized.jpg"
        img.save(temp_path)
        resized_images.append(temp_path)

    num_images = len(resized_images)

    # Step 2: Load audio and get duration
    if music_path:
        audio = AudioFileClip(music_path)
        audio_duration = min(audio.duration, max_audio_duration)  # Clamp to 30 seconds max
    else:
        audio = None
        audio_duration = num_images  # fallback: 1 sec per image

    # Step 3: Calculate image duration & fps
    duration_per_image = audio_duration / num_images
    fps = 1 / duration_per_image  # e.g. 1 image every 2s = 0.5fps

    # Step 4: Create video clip
    clip = ImageSequenceClip(resized_images, fps=fps)

    if audio:
        audio = audio.subclipped(0, clip.duration)
        clip = clip.with_audio(audio)

    # Step 5: Write final video
    clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

    # Step 6: Cleanup
    for temp_img in resized_images:
        os.remove(temp_img)

    return output_path
