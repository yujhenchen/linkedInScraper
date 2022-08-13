#!/bin/bash

VENV_NAME=scraper_work_env

# Show conda information
conda update -y conda
conda info
conda env list

# Create environment with specific python version and activate
conda create -n $VENV_NAME python=3.9 -y -f
conda activate $VENV_NAME
