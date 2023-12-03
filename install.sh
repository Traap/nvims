#!/bin/bash

# Copy files to their production locations.
sudo cp -v nvims /usr/local/bin/.
sudo chmod -v +x /usr/local/bin/nvims

mkdir -p "$HOME"/.config/nvims
cp -v neovim_distros "$HOME"/.config/nvims/.
