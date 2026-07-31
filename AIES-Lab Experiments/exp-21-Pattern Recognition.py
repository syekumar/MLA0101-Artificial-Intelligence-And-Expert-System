import cv2
import matplotlib.pyplot as plt
import os

image_path = r"C:\Users\Sye Kumar\OneDrive\Pictures\Screenshots\Screenshot 2026-07-30 132831.png"

if not os.path.exists(image_path):
    print("Image not found!")
    exit()

image = cv2.imread(image_path)

if image is None:
    print("Unable to load image!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

print("Pattern Recognition Completed Successfully")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(edges, cmap="gray")
plt.title("Detected Pattern (Edges)")
plt.axis("off")

plt.tight_layout()
plt.show()
