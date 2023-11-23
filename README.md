## nvims
Safely experiment with multiple Neovim configurations.

A repository defined in bash variable neovim_apps is cloned into $HOME/.config.

## Nvim Operational modes
nvims installs or removes a Neovim configuration.

### Install a Neovim configuration.
```
nvim
```

### Remove a Neovim configuration.
```
nvim -d
```

### Keybindings

| Keybind    | Action                   |
| :--------- | : ---------------------- |
| <c-c>      | Cancel.                  |
| <c-p>      | Previous selection       |
| <c-n>      | Next selection           |
| <enter>    | Selecte highlighted item |

## Neovim configurations supported as of 2023-11-13
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
``
