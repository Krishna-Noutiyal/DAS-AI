"""
Datasets Package

This package contains datasets and utilities for working with categorized data
with depression, anxiety, and stress scores.

Modules:
- dataset: Contains functions and classes for loading and processing datasets.

Files:
- categorized_datav4_scored.csv: A CSV file with categorized data and scoring.

Author: [Your Name or Organization]
"""

from .dataset import load_dataset, validate_dataset, show_datasets

__all__ = ["load_dataset", "validate_dataset","show_datasets"]