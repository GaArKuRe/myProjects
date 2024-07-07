import os
import time

os.chdir("/home/gaddampally.reddy/Pictures/Screenshots")
screenshots = os.listdir()
base_path = "/home/gaddampally.reddy/"
file_path = "/home/gaddampally.reddy/Pictures/Screenshots/"

sgfm_path = base_path + "Pictures/SGFM/"
amt_path = base_path + "Pictures/AMT/"
gjld_path = base_path + "Pictures/GJLD/"
ml_path = base_path + "Pictures/ML/"
mgc_path = base_path + "Pictures/MGC/"
mct_path = base_path + "Pictures/MCT/"
# moving screenshots to respective folders
for screenshot in screenshots:
    if "sgfm_" in screenshot:
        print(f"moving file {screenshot} to SGFM folder")
        os.replace(file_path+screenshot, sgfm_path+screenshot)
        screenshots.remove(screenshot)
    elif "amt_" in screenshot:
        print(f"moving file {screenshot} to SGFM folder")
        os.replace(file_path+screenshot, sgfm_path+screenshot)
        screenshots.remove(screenshot)
    elif "gjld_" in screenshot:
        print(f"moving file {screenshot} to SGFM folder")
        os.replace(file_path+screenshot, sgfm_path+screenshot)
        screenshots.remove(screenshot)
    elif "ml_" in screenshot:
        print(f"moving file {screenshot} to SGFM folder")
        os.replace(file_path+screenshot, sgfm_path+screenshot)
        screenshots.remove(screenshot)
    elif "mgc_" in screenshot:
        print(f"moving file {screenshot} to SGFM folder")
        os.replace(file_path+screenshot, sgfm_path+screenshot)
        screenshots.remove(screenshot)
    elif "mct_" in screenshot:
        print(f"moving file {screenshot} to SGFM folder")
        os.replace(file_path+screenshot, sgfm_path+screenshot)
        screenshots.remove(screenshot)



print("Deleting unnamed screenshots older than a week")
latest_screenshots = list()
for screenshot in screenshots:
    creation_time = os.path.getctime(file_path+screenshot)
    current_time = time.time()
    if "Screenshot from" in screenshot:
        if (current_time - creation_time) > 604800:
            os.remove(screenshot)
        else:
            latest_screenshots.append(screenshot)

print("latest screenshots which are not older than a week are listed below")
print(latest_screenshots)
