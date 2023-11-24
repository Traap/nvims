# nvims
Safely experiment with multiple Neovim configurations.

![Nvims screenshot](https://github.com/Traap/nvims/blob/master/nvims.png)

## Nvim Operational modes
nvims installs or removes a Neovim configuration.

### Install nvims
```bash
sudo sh -c 'curl -fLo "/usr/local/bin"/nvims \
       https://raw.githubusercontent.com/traap/nvims/master/nvims' \
    && sudo chmod +x /usr/local/bin/nvims
```

### Install a Neovim configuration.
```
nvim
```

### Remove a Neovim configuration.
```
nvim -d
```

### Keybindings
| Keybind | Action
| ---     | ---
| ctrl-c  | Cancel.
| ctrl-p  | Previous selection
| ctrl-n  | Next selection
| enter   | Selecte highlighted item

## Neovim configurations supported.
```bash
# alias      | Github repository       | default or branch name
readonly neovim_apps=(
  "astro     | AstroNvim/AstroNvim     | default"
  "asyncedd  | asyncedd/dots.nvim      | default"
  "barebones | Traap/barebones         | default"
  "baretmux  | Traap/barebones         | tmux"
  "default   | none                    | none"
  "exos      | exosyphon/nvim          | none"
  "kickstart | nvim-lua/kickstart.nvim | default"
  "nvchad    | NvChad/NvChad           | default"
  "nvconf    | TechnicalDC/NvConf      | default"
  "prime     | Traap/init.lua          | default"
  "prune     | Traap/nvim              | prune"
  "starter   | LazyVim/starter         | default"
  "traap     | Traap/nvim              | default"
  "vapour    | Traap/VapourNvim        | default"
  "void      | nvoid-lua/nvoid         | default"
  "zero      | Traap/lazy.zero         | default"
  "zulu      | Traap/nvim              | v0.6.8-packer"
)
```
Note: see nvims file for latest configuration packages supported.
