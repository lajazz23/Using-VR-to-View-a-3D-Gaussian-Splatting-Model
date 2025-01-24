import os
import subprocess

path = "C:/Users/jlin3/gaussian-splatting"

subject = input('What is the name of your subject? ')
print('Okay! Your subject has been named', subject,'!')

mini_path_in = 'input_data/' + str(subject)
mini_path_out = 'C:/Users/jlin3/gaussian-splatting/output/room/' + str(subject)

colmap_execution = 'python convert.py -s ' + mini_path_in + ' --colmap_executable "C:/Users/jlin3/colmap-x64-windows-cuda/COLMAP.bat"'
print(colmap_execution)

optimizer = 'python train.py -s ' + mini_path_in
print(optimizer)

output_path = 'SIBR_gaussianViewer_app.exe -m ' + mini_path_out
print(output_path)

commands = [
    'conda activate gaussian_splatting',
    'cd C:/Users/jlin3/gaussian-splatting',
    colmap_execution,
    optimizer,
    'cd C:/Users/jlin3/gaussian-splatting-Windows/viewers/bin',
    output_path
]

cmd_commands = " && ".join(commands)

subprocess.Popen(f'start cmd /K "{cmd_commands}"', shell=True)

