# Using VR to View a 3D Gaussian Splatting Model
This repository is a record of how I sucessfully modeled 3D Gaussian Splatting and viewed it in a virtual reality environment. 

## 3D Gaussian Splatting
Original paper: [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_high.pdf)
Original repository: https://github.com/graphdeco-inria/gaussian-splatting

3D Gaussian splatting is a method of rebuilding a 3D scene using gaussian splats. Gaussian splats hold information such as covariance, position, color, and opacity. Together, the gaussian splats create a continuous radiance field. 

## Requirements

### Hardware
- **PC:** Alienware Aurora R16 (x64)
- **Processor:** Intel(R) Core(TM) i9-14900KF   3.20 GHz
- **RAM:** 64.0 GB
- **GPU:** NVIDIA GeForce RTX 4090

### Software

These were installed in sequential order.
- **[Git](https://git-scm.com/downloads) :** To be used for cloning the repository to obtain the code.
- **[Conda](https://www.anaconda.com/download/success) :** To be used to create the environment that the code utilizes.
- **[CUDA Toolkit v11.7](https://developer.nvidia.com/cuda-11-7-1-download-archive) :** The version of CUDA is critical for the success of the code. 
- **[Visual Studio 2022 v17.4.6](https://www.catalog.update.microsoft.com/Search.aspx?q=visual+studio+2022&p=3) :** Be sure to select **Desktop development with C++**, as well as **MSVC v142 - VS 2019 C++ x64/x86 build tools**. 
- **[COLMAP](https://github.com/colmap/colmap/releases) :** Used for reconstruction of 3D scene from images.
- **[ImageMagik](https://imagemagick.org/script/download.php) :** Used for formatting and preparing images.
- **[FFmpeg](https://ffmpeg.org/download.html) :** Used for extracting images from videos.

## Setup
Before touching the code, ensure that:
- "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64" is added to the PATH.
- CUDA toolkit has been installed.
- Visual Studio 2022 is version 17.4.6. I didn't find success using the latest version of Visual Studio 2022.

I used Windows Command Prompt for the initial setup and optimizing for the code. Be sure to close and reopen a new cmd window everytime you make manual file changes.

### Cloning the Repository
I first cloned the repository, which could be found in the ``C:User/<username>`` folder.
```
git clone https://github.com/graphdeco-inria/gaussian-splatting --recursive
```
### Installing the Optimizer
To install the optimizer, I created a Conda environment. 

``conda create -n gaussian_splatting python=3.7``

``conda activate gaussian_splatting``

NOTE: Always activate the gaussian_splatting environment before executing code.

``conda install -c conda-forge vs2022_win-64
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117``

NOTE: Certain versions of PyTorch and CUDA are not compatible. The versions above worked well for me.

### Installing Submodules
In the initial setp of the environment, the submodules did not install properly. It will  be done here. 

``cd C:\Users\<username>\gaussian-splatting``

``pip install submodules/diff-gaussian-rasterization``

``pip install submodules/simple-knn``

``pip install plyfile``

``pip install tqdm``

If the above did not work, please consult the errors section below.

## Data Preparation
Both videos and images can be used. 
First, I renamed the video for clarity and moved it into ``../gaussian-splatting/input_data``. For example, with a video called ``room.mp4``:

```
📂.../ 
├──📂gaussian-splatting/ 
│   ├──📂input_data/
│   │	├──room.mp4		
│   │   │...
│   │...
│...
```

Now, opening Command Prompt again, input:
```
conda activate gaussian_splatting
cd gaussian-splatting
```
With the video in the correct location, input:
```
ffmpeg -i input_data/room.mp4 -r 1/1 input_data/room/image%03d.png
```
This will output a series of images inside ``../gaussian-splatting/input_data/room``. 

Images need to be setup in a specific way so that COLMAP can recognize it. I created another folder and manually moved the images into it. The structure is seen below:

```
📂.../ 
├──📂gaussian-splatting/ 
│   ├──📂input_data/
│   │	├──📂room/
│   │	│	├──📂input/
│   │	│	│	├── 🖼️ <image 0>
│   │	│	│	├── 🖼️ <image 1>
│   │	│	│	│...
│   │   │...
│   │...
│...
```
For optimization to work, COLMAP needs to format the images properly.
```
python convert.py -s input_data/room --colmap_executable "C:\Users\<username>\colmap-x64-windows-cuda\COLMAP.bat"
```
NOTE: COLMAP may be installed in a different location on your computer. Just change the path of COLMAP accordingly.

## Optimizing the data
With the Conda environment active and the correct directory on Command Prompt, input:

```
python train.py -s input_data/room
```

This step takes the longest. The code will generate a new folder in ````../gaussian-splatting/output`` that will contain the data. The name of the folder is usually randomized. I changed the name of this folder for clarity. The structure can be seen below:

```
📂.../ 
├──📂gaussian-splatting/ 
│   ├──📂output/
│   │	├──📂room/ # original name was "ade9c340-8"
│   │	│	├──📂point_cloud/
│   │	│	│	├──📂iteration_7000/
│   │	│	│	├──📂iteration_30000/ 
│   │	│	│...		
│   │   │...
│   │...
│...
```

## Viewing the 3D Gaussian Splats in SIBR
The original repository uses SIBR to view the generated model, called``SIBR_gaussianViewer_app.exe``. You can find it [here](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/binaries/viewers.zip).

Extract the zip file and move it to the ``../gaussian-splatting`` folder. 

To set it up:

```
cd viewers/bin

```




```
cd C:\Users\username\gaussian-splatting-Windows\viewers\bin
```
```
SIBR_gaussianViewer_app.exe -m <folder containing point_cloud>
```
