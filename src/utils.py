import os
import sys
import dill
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        # Get directory path and ensure it exists
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        # Save the object to the specified file path using dill
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
