from ultralytics import YOLO
import cv2
import os
import shutil

# load model
model = YOLO('runs/detect/train19/weights/best.pt')
lake_folder = "OSM_lakecontours"  # input images


results_folder = "0SM_DETECTIONS"
shutil.rmtree(results_folder)  # clean the folder
os.makedirs(results_folder, exist_ok=True)

files = [file for file in os.listdir(lake_folder)]

confidence_threshold = 0.85  # set confidence threshold

for i, file_name in enumerate(files):

    file_path = os.path.join(lake_folder, file_name)
    image = cv2.imread(file_path)
    # do the detection
    results = model(image, conf=confidence_threshold)

    # if any detections
    if len(results[0].boxes) > 0:
        conf = results[0].boxes.conf[0]  # get the confidence of the first detection
        print(f"confidence of first detection: {conf}")

        # save the image if confidence is above the threshold
        annotated_image = results[0].plot()  # plot() draws the bounding boxes and labels on the image
        output_path = os.path.join(results_folder, f"{file_name}.png")
        cv2.imwrite(output_path, annotated_image)
        print(f"saved detected object to {output_path} with confidence {conf}")
    else:
        print(f"no detection in {file_name}")
