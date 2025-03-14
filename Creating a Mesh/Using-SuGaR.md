A common issue with vanilla 3D Gaussian Splatting (3D GS) is the lack of a physical collider within Unity VR. Without a mesh, the rays from the controllers peirce through the splats and render them undetectable. To combat this issue, I used [SuGaR](https://github.com/Anttwo/SuGaR?tab=readme-ov-file) to export the mesh from the original model. Then, I implemented this mesh into Unity to allow for the rays to intersect with the mesh, now situated inside the 3D GS model.

```
python train_full_pipeline.py -s /mnt/c/Users/<username>/gaussian-splatting/input_data/room -r "dn_consistency" --high_poly True --export_obj True --gs_output_dir /mnt/c/Users/<username>/gaussian-splatting/output/room
```

After extracting the mesh, I import it into [MeshLab](https://www.meshlab.net/) to prune it and remove excess noise. I can then import this edited mesh into Unity, where it will situate itself inside of the 3D GS model.
