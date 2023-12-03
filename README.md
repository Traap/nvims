# nvims
Safely experiment with multiple Neovim configurations.

![Nvims screenshot](https://github.com/Traap/nvims/blob/master/nvims.png)

## Nvim Operational modes
nvims installs or removes a Neovim configuration.

### Install nvims

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Traap/nvims/master/install.sh)"
```
### Uninstall nvims
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Traap/nvims/master/uninstall.sh)"
```

### Install a Neovim configuration.
```
nvims
```

### Remove a Neovim configuration.
```
nvims -d
```

### Keybindings
| Keybind | Action
| ---     | ---
| ctrl-c  | Cancel.
| ctrl-p  | Previous selection
| ctrl-n  | Next selection
| enter   | Selecte highlighted item

## Neovim configurations supporte.
```bash
# alias      | Github repository       | efault or branch name
readonly neovim_distros=(
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
  "zero      | Traap/lazy.zero         | "
  "zulu      | Traap/nvim              | v0.6.8-packer"
)
```
Note: see nvims file for latest configuration packages supported.

## Suggested bash login change
```bash
if [[   -f "$HOME/.config/nvims/nvim_appnames" ]]; then
	source "$HOME/.config/nvims/nvim_appnames"
fi
```
