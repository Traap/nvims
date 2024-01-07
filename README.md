# nvims
Safely experiment with multiple Neovim configurations.

![Nvims screenshot](https://github.com/Traap/nvims/blob/master/nvims.png)

## Nvim Operational modes
nvims installs or removes a Neovim configuration.

### Requirements 
- [fzf](https://github.com/junegunn/fzf)

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

## Neovim configurations supported.
```bash
# alias      | Github repository       | default or branch name
readonly neovim_distros=(
  "LazyVim   | LazyVim/starter         | default"
  "OVIwrite  | MiragianCycle/OVIWrite  | default"
  "astro     | AstroNvim/AstroNvim     | default"
  "asyncedd  | asyncedd/dots.nvim      | default"
  "barebones | Traap/barebones         | default"
  "baretmux  | Traap/barebones         | tmux"
  "CyberNvim | pgosar/CyberNvim        | default"
  "default   | none                    | none"
  "exos      | exosyphon/nvim          | none"
  "kickstart | nvim-lua/kickstart.nvim | default"
  "lervag    | lervag/dotnvim          | default"
  "nvchad    | NvChad/NvChad           | default"
  "nvconf    | TechnicalDC/NvConf      | default"
  "prime     | Traap/init.lua          | default"
  "pwnvim    | pwnwriter/pwnvim        | default"
  "traap     | Traap/nvim              | default"
  "vapour    | Traap/VapourNvim        | default"
  "void      | nvoid-lua/nvoid         | default"
  "xray      | Traap/nvim              | v0.9.5-lazyvim"
  "zero      | Traap/lazy.zero         | default"
  "zulu      | Traap/nvim              | v0.6.8-packer"
)
```
Note: see
[neovim_distros](https://github.com/Traap/nvims/blob/master/neovim_distros)
file for latest configuration packages supported.

## Suggested bash login change
```bash
if [[   -f "$HOME/.config/nvims/nvim_appnames" ]]; then
	source "$HOME/.config/nvims/nvim_appnames"
fi
```

## So, you want to add your Neovim configuration so others can use it?
1. Make a pull-request that updates neovim_distro with your GitHub URL and Branch.
2. Your Neovim configuration *MUST* bootstrap itself.
3. I'll test it on either Arch or Ubuntu.
4. With 1, 2, and 3 passing. I'll merge your pull-request.

