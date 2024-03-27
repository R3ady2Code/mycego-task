from PIL import Image
import os

main_dir_path = 'Для тестового'

# Динамический параметры, которые можно менять
image_formats = ('.png', '.jpg', '.jpeg', '.gif') # Список форматов, которые мы считаем изображением
padding = 80
collage_background = (255, 255, 255)

def collect_images_from_folders(folder_names):
    images = []
    for folder_name in folder_names:
        folder_path = os.path.join(main_dir_path, folder_name) 
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith(image_formats): 
                    image_path = os.path.join(folder_path, filename)
                    image = Image.open(image_path)
                    images.append(image)
    return images

def create_image_collage(images, output_filename):
    image_width, image_height = images[0].size

    images_per_row = min(len(images), 4)
    num_rows = (len(images) + images_per_row - 1) // images_per_row

    # Определяем размеры коллажа с учетом увеличенных отступов и отступов с краю коллажа
    collage_width = images_per_row * (image_width + padding) + padding
    collage_height = num_rows * (image_height + padding) + padding

    collage = Image.new('RGB', (collage_width, collage_height), collage_background)
    current_x = padding  # Задаем начальные координаты равные отступу, поскольку нам нужны отступы по краям коллажа
    current_y = padding
    for img in images:
        collage.paste(img, (current_x, current_y))
        current_x += image_width + padding 
        if current_x >= collage_width:
            current_x = padding
            current_y += image_height + padding

    collage.save(output_filename)
    print(f"Коллаж успешно сохранен в файл {output_filename}")

def generate_tif(folder_names):
    all_images = collect_images_from_folders(folder_names)
    output_filename = 'Result.tif'
    create_image_collage(all_images, output_filename)


folder_names = ['1388_12_Наклейки 3-D_3', '1388_6_Наклейки 3-D_2']
generate_tif(folder_names)
