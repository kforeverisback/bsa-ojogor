#!/bin/bash

sudo chown -R 1000:1000 /workspaces/
sudo chown -R 1000:1000 /opt/conda
/opt/conda/bin/conda init zsh
/opt/conda/bin/conda config --set auto_activate_base False