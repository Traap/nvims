#!/bin/bash
set -e

# Use a private checkout and remove only the directory created by this run.
install_tmp=$(mktemp -d)
trap 'rm -rf -- "$install_tmp"' EXIT

git clone https://github.com/Traap/nvims "$install_tmp/nvims"
cd "$install_tmp/nvims"

sudo install -m 755 nvims /usr/local/bin/nvims
mkdir -p "$HOME/.config/nvims"
cp -v neovim_distros "$HOME/.config/nvims/"

echo "Installation complete."
echo "Add /usr/local/bin to your PATH if it's not already."
