import cv2

# Read the images
img1 = cv2.imread("/home/aayush/Aryans_RoboVision_Takneek25/src/robot_pointcloud_project/data/images/img.png")
img2 = cv2.imread("/home/aayush/Aryans_RoboVision_Takneek25/src/robot_pointcloud_project/data/images/img_1.png")
img3 = cv2.imread("/home/aayush/Aryans_RoboVision_Takneek25/src/robot_pointcloud_project/data/images/img_2.png")

# Put them into a list
images = [img1, img2, img3]

# Create a stitcher object
stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)  # for OpenCV 4.x

# Stitch the images
(status, stitched) = stitcher.stitch(images)

# Check if stitching succeeded
if status == cv2.Stitcher_OK:
    print("Stitching completed successfully.")
    cv2.imwrite("stitched_output.jpg", stitched)
    cv2.imshow("Stitched Image", stitched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Stitching failed. Error code:", status)
