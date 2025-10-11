import os 
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
            
@ensure_annotations  #annotation: comment that specifies the expected types of function arguments and return values.
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input 
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    
    
@ensure_annotations # i need this to get model evaluation for loss and evaluation metrics
def save_json(path: Path, data: dict):
    '''save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file'''
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data,f,indent = 4)     #indent=4. Makes the JSON output pretty-printed with an indentation of 4 spaces.
        
    logger.info(f'json file saved at: {path}')
    
    
@ensure_annotations
def save_bin(data:Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file 
    """
    joblib.dump(value = data, filename=path)
    logger.info(f'binary file saved at: {path}')
    

@ensure_annotations
def load_bin(path: Path):
    """load binary data
    Args: 
        path (Path): path to binary file
        
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from:{path}")
    return data


@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path of the file
        
    Returns:
        str: size in KB
    """
    size_in_bytes = path.stat().st_size  # Get size in bytes
    size_in_kb = round(size_in_bytes / 1024)
    return f"~{size_in_kb} KB"


def decodeImage(imgstring, fileName): #convert image to Base64 (convert image to into a text string)
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath): # decodes the Base64 string back into binary data (original image bytes)
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())
    
    