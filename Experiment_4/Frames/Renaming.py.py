import os

os.chdir('Experiment_4/Frames')
print(os.getcwd())

for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "frame" + str(count)

    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
