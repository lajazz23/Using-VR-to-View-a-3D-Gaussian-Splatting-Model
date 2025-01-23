# Using VR to View a 3D Gaussian Splatting Model
This repository is a record of how I sucessfully modeled 3D Gaussian Splatting and viewed it in a virtual reality environment. Please also review the original repository.

There are two sections to this repository:

1. [3D Gaussian Splatting](#3d-gaussian-splatting)
2. [3D Gaussian Splatting in Unity](#using-vr-to-view-a-3d-gaussian-splatting-model)

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
- **[CUDA Toolkit v11.7](https://developer.nvidia.com/cuda-11-7-1-download-archive) :** The version of CUDA is critical for the success of the code. Version 11.6 will not work, and 11.8 did not work for me.
- **[Visual Studio 2022 v17.4.6](https://www.catalog.update.microsoft.com/Search.aspx?q=visual+studio+2022&p=3) :** Be sure to select **Desktop development with C++**, as well as **MSVC v142 - VS 2019 C++ x64/x86 build tools**. 
- **[COLMAP](https://github.com/colmap/colmap/releases) :** Used for reconstruction of 3D scene from images.
- **[ImageMagik](https://imagemagick.org/script/download.php) :** Used for formatting and preparing images.
- **[FFmpeg](https://ffmpeg.org/download.html) :** Used for extracting images from videos.

## Setup
Before touching the code, ensure that:
- ``C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64`` is added to the PATH. This should be the 2019 toolkit. 
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
In the initial setup of the environment, the submodules did not install properly. It will  be done here. 

``cd C:\Users\<username>\gaussian-splatting``

``pip install submodules/diff-gaussian-rasterization``

``pip install submodules/simple-knn``

``pip install plyfile``

``pip install tqdm``

NOTE: I had failed installing the submodules many times. Using the Visual Studio 2019 C++ toolkit seemed to fix the issue. 

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
cd C:\Users\<username>\gaussian-splatting\viewers\bin

SIBR_gaussianViewer_app.exe -m C:\Users\<username>\gaussian-splatting\output\room
```
This should open the viewer, of which you can explore the model in.


# Unity Gaussian Splatting
To view the 3D Gaussian Splatting model in Unity, I utilized the [Gaussian Splatting playground in Unity](https://github.com/aras-p/UnityGaussianSplatting) repository.

## Requirements

### Hardware
- Meta Quest Pro
- Meta Quest Link cable

### Software
- **[Unity 2022.3.7](https://unity.com/releases/editor/whats-new/2022.3.7) :** Newer versions of Unity may work as well.

## Setup
Clone the repository to have access to the toolkit.

```
git clone https://github.com/aras-p/UnityGaussianSplatting
```

In Unity Hub, open the file ``../<username>\UnityGaussianSplatting\projects\GaussianExample`` and open **GSTestScene** in Unity.

### Unity Setup
Inside Unity, navigate to ``Window > Package Manager``. Inside the Package Manager, install:
- OpenXR Plugin
- XR Plugin Management
- XR Interaction Toolkit
- Post-Processing

After installing the packages, navigate to ``Edit > Project Settings``. 
- In **XR Plugin Management**, ensure that ``OpenXR`` is selected under the Plug-in Providers tab.
- Under **XR Plugin Management**, navigate to **OpenXR** and change the Render Mode to ``Multi-pass``.
- Under **XR Plugin Management**, navigate to **Project Validation** and fix all of the errors by clicking the ``Fix All`` button.

## Importing the Generated 3D Gaussian Splatting Model
In the previous section, we generated a 3D Gaussian Splatting Model of a scene. It can be found in the folder ``C:\Users\<username>\gaussian-splatting\output\room``
Back in Unity, go to ``Tools > GaussianSplats > Create GaussianSplatAsset``. This should open a window that will allow for importing the .ply file. Select the .ply file, found in the folders in  ``C:\Users\jlin3\gaussian-splatting\output\room\point_cloud\...``.

Select ``Create Asset``, and it should show up within GaussianAssets.

## Viewing the Model
In the Hierarchy tab of Unity, create a new Game Object and name it accordingly. Go to its properties:
- add **Gaussian Splat Renderer** and select the asset that was just imported.
- add **Post-Process Layer**, and set the Layer to ``Everything``.

Next, add a Camera under the Game Object. In its Properties, add a **Tracked Pose Driver**. This will allow the scene to be static when viewed in VR. 

Connect the Meta Quest Pro to the computer via Quest Link. Inside, you should be able to view the desktop and control it remotely. Select Unity from the Desktop inside the Quest Pro, and press the **Play** button on the top.