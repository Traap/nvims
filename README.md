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

### OSX additional instructions
See issue ![#8](https://github.com/Traap/nvims/issues/8) for Bash and OSX discussion.

```
brew install bash
echo /usr/local/bin/bash | sudo tee -a /etc/shells
sed -i '1 s/^.*$/\#\!\/usr\/local\/bin\/env bash/' /usr/local/bin/nvims
```

### Install a Neovim configuration.
Your selection is written to `~/.config/nvims/nvim_appnames`.

```
nvims
```

### Remove a Neovim configuration.
Used to an existing distribution when it exists.  The distribution also removed
from `~/.config/nvims/nvim_appnames`.
```
nvims -d
```

### Reset a Neovim configuration.
Used to reset an existing distribution when it exists.  The distribution is not
cloned or pulled, but it is bootstrapped when Neovim is started.
```
nvims -r
```

### Set Neovim default configuration.
 default is one of the Neovim distribution nvim provides.  Normally, this means
 nvim will launch Neovim similar to using `nvim -u NORC`.  This changes when
 nvim -s is used.  Firstly, your selection is written to
 `~/.config/nvims/nvim_default_app` Secondly, when you run nvims and select
 `default`, nvims will figure use your default.

Your selection is written to `~/.config/nvims/nvim_appnames` and to
`~/.config/nvims/nvim_default_app`.
```
nvims -s
```

### Nvims usage
```
nvims -h
```
Usage: nvims [] [-d] [-r] [-s] [-h]

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
  "default    | none                    | none"
  "astro      | AstroNvim/AstroNvim     | default"
  "asyncedd   | asyncedd/dots.nvim      | default"
  "barebones  | Traap/barebones         | default"
  "baretmux   | Traap/barebones         | tmux"
  "cam        | ChristianChiarulli/nvim | default"
  "CyberNvim  | pgosar/CyberNvim        | default"
  "exos       | exosyphon/nvim          | none"
  "kickstart  | nvim-lua/kickstart.nvim | default"
  "launch     | LunarVim/Launch.nvim    | default"
  "LazyVim    | LazyVim/starter         | default"
  "lervag     | lervag/dotnvim          | default"
  "NormalNvim | NormalNvim/NormalNvim   | default"
  "nvchad     | NvChad/NvChad           | default"
  "nvconf     | TechnicalDC/NvConf      | default"
  "OVIwrite   | MiragianCycle/OVIWrite  | default"
  "prime      | Traap/init.lua          | default"
  "pwnvim     | pwnwriter/pwnvim        | default"
  "traap      | Traap/nvim              | default"
  "vapour     | Traap/VapourNvim        | default"
  "void       | nvoid-lua/nvoid         | default"
  "xray       | Traap/nvim              | v0.9.5-lazyvim"
  "zero       | Traap/lazy.zero         | default"
  "zulu       | Traap/nvim              | v0.6.8-packer"
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

## Update notification
1. nvims appends to ```~/.config/nvims/nvim_appnames```
2. nvims does not remove entries from ```~/.config/nvims/nvim_appnames``` when
   ```nvims -d``` option is used.
3. A future update will reconcile ```~/.config/nvims/nvim_appnames``` with
   ```neovim_distros``` actually installed.

