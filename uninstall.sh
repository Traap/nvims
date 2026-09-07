#!/bin/bash
set -e

# Remove all files nvims installed or created.
sudo rm -fv /usr/local/bin/nvims
rm -rfv "$HOME"/.config/nvims
