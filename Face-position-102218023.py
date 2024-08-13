import os
import csv
from PIL import Image
from landingai.predict import Predictor


model_endpoint = "90b45bc5-6029-4a94-8acc-dc2735081e39"
access_key = "land_sk_7VVG8HeQUOjnENhi5ZoE6yL0H8sl4IURmmwvj7Zh6l620u1sGk"
input_directory = "Google_images"
output_file = "predictionsoffaces.csv"


predictor_instance = Predictor(model_endpoint, api_key=access_key)
image_list = [img for img in os.listdir(input_directory) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))][:200]
total_images = len(image_list)


with open(output_file, mode='w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Image Name", "Score", "Label Name", "Label Index"])

    for idx, img_name in enumerate(image_list, start=1):
        img_path = os.path.join(input_directory, img_name)
        image = Image.open(img_path)

        
        results = predictor_instance.predict(image)

        for result in results:
            score_value = result.score
            label = result.label_name
            label_id = result.label_index

            
            csv_writer.writerow([img_name, score_value, label, label_id])
        print(f"Completed {idx}/{total_images} images")

print(f"Prediction results have been saved to {output_file}")
