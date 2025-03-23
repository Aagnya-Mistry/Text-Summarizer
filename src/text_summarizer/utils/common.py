import os
from box.exceptions import BoxValueError
from text_summarizer.logging import logger
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns 
    
    Args:
        path_to_yaml (str): path like input

    Raises:
        BoxValueError: If the yaml file is not found
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yamle file: {path_to_yaml} read successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_dir(dir_path: list, verbose=True):
    """
    Create directory if not exists
    
    Args:
        dir_path (list): List of directory paths
        verbose (bool): Print logs
    
    Returns:
        None
    """
    for path in dir_path:
        if not os.path.exists(path):
            os.makedirs(path)
            if verbose:
                logger.info(f"Directory created: {path}")
        else:
            if verbose:
                logger.info(f"Directory already exists: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size of the file
    
    Args:
        path (str): Path of the file
    
    Returns:
        str: Size of the file
    """
    size_in_kb = round(os.path.getsize(path)/1024,2)
    return size_in_kb