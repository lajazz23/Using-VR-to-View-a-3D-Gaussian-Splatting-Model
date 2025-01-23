# Using-VR-to-View-a-3D-Gaussian-Splatting-Model
This repository is just a record of how I sucessfully modeled 3D Gaussian Splatting and viewed it in a virtual reality environment. I used the official implementation of the paper, "3D Gaussian Splatting for Real-Time Radiance Field Rendering"


ffmpeg -i input_data/filename.mp4 -r 1/1 input_data/bottle/filename%03d.png
python convert.py -s input_data/filename --colmap_executable "C:\Users\username\colmap-x64-windows-cuda\COLMAP.bat"
python train.py -s input_data/filename
cd C:\Users\username\gaussian-splatting-Windows\viewers\bin
SIBR_gaussianViewer_app.exe -m <folder containing point_cloud>
