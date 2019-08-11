"""Utility functions for PyTorch."""
import torch


def np_to_torch(self, dict):
    """
    Convert numpy arrays to PyTorch tensors.

     Args:
        dict (dict): Dictionary of data in numpy arrays.

    Returns:
       Dictionary of data in PyTorch tensors.

    """
    for key, value in dict.items():
        dict[key] = torch.FloatTensor(value)
    return dict

def torch_to_np(self, value_in):
    """
    Convert PyTorch tensors to numpy arrays.

     Args:
        value_in (tuple): Tuple of data in PyTorch tensors.

    Returns:
       Tuple of data in numpy arrays.

    """
    value_out = []
    for v in value_in:
        value_out.append(v.numpy())
    return tuple(value_out)
