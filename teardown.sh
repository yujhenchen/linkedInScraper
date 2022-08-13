#!/bin/bash

VENV_NAME=scraper_work_env

conda deactivate
conda env remove --name $VENV_NAME

# Print the base envs
ENV_BASE=$(conda-env list | awk '/base/ { print $NF }')
echo $ENV_BASE
# Delete the target env
rm -rf "$ENV_BASE/envs/$VENV_NAME"

conda env list
