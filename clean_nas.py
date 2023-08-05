import os
import shutil

def remove_pytorch_model_bin(folder_path):
    shots_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20', '30', '40', '50']
    # print(f"Checking {folder_path}")
    for root, dirs, files in os.walk(folder_path):
        # print(f"Checking {root}")
        # print(f"Checking {dirs}")
        for dir_name in dirs:
            if dir_name.startswith("fewshots"):
                for shots in shots_list:
                    subdir_path = os.path.join(root, dir_name)
                    subdir_path += f"/percent-{shots}/google/mt5-smallmt5_except_domain_none_slotlang_slottype_lr_0.0001_epoch_5_seed_457"
                    pytorch_model_bin_path = os.path.join(subdir_path, "pytorch_model.bin")
                    print(f"Checking {pytorch_model_bin_path}")
                    if os.path.isfile(pytorch_model_bin_path):
                        os.remove(pytorch_model_bin_path)
                        print(f"Removed {pytorch_model_bin_path}")
                    last_checkpoint = os.path.join(subdir_path, "lightning_logs")
                    shutil.rmtree(last_checkpoint, ignore_errors=True)
# Provide the root folder path where the search should start


def remove_lightning_logs(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            if dir_name == 'lightning_logs':
                logs_folder_path = os.path.join(root, dir_name)
                shutil.rmtree(logs_folder_path, ignore_errors=True)
                print(f"Deleted folder: {logs_folder_path}")

# Provide the parent directory path where the search should start
# parent_directory = "./output/arabic/mt5/small/5epochs"
parent_directory = "./output/french/mt5/"

remove_lightning_logs(parent_directory)

# remove_pytorch_model_bin(parent_directory)
