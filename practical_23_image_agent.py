from transformers import pipeline


# Load image classification model
classifier = pipeline(
    "image-classification",
    model="google/mobilenet_v2_1.0_224"
)


# Get image path
image = input("Enter image path: ")


# Classify image
results = classifier(image)


# Get prediction
label = results[0]["label"]
score = results[0]["score"]


# Display perception
print("\nPerception:", label)
print("Confidence:", round(score, 2))


# Agent decision
if score > 0.7:
    print("Agent Action: Accept prediction")
else:
    print("Agent Action: Request human review")