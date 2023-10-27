import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'deep-span-402803-1e142b189014.json'

client = vision.ImageAnnotatorClient()

file_name = r'picture.png'
image_path = f'.\{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
response = client.label_detection(image=image)
labels = response.label_annotations

df = pd.DataFrame(columns=['description', 'score', 'topicality'])

for annotation in labels:
    description = annotation.description
    score = annotation.score
    topicality = annotation.topicality

    # You can use this data as needed in your Python code
    print(f"Label: {description}, Score: {score}, Topicality: {topicality}")

"""for label in labels:
    df = df._append(
        dict(
            description=label.description,
            score=label.score,
            topicality=label.topicality,

        ), ignore_index=True
    )
print(df)"""