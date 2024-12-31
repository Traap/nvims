# nvims
Safely experiment with multiple Neovim configurations.

![Nvims screenshot](https://github.com/Traap/nvims/blob/master/nvims.png)

## Nvim Operational modes
nvims deletes, installs, resets or sets a default nvims configuration.

nvims **does not** modify the followin Neovim directories.
* ~/.config/nvim
* ~/.cache/nvim
* ~/.local/share/nvim
* ~/.local/state/nvim

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
default is one of the Neovim distribution nvims provides.  Normally, this
means nvims will launch Neovim similar to using "nvim -u NORC".  This changes
when nvims -s is used.  Firstly, $defaultNeovimDistro is written to with your
desired default. Secondly, when you run nvims and select "default", nvims
will set $choice to $defaultNeovimDistro.

Your selection is written to `~/.config/nvims/nvim_appnames` and to
`~/.config/nvims/nvim_default_app`.
```
nvims -s
```

### Nvims usage
```
nvims -h
```
```log
Usage: nvims [] [-d] [-r] [-s] [-h]
 [ ] - Display nvim selection list.
 [d] - Delete selected nvimapp installation.
 [r] - Reset selected nvimapp installation.
 [s] - Set selected nvimapp as nvims default.
 [h] - Display this message.
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
# alias       | sn  | URL                     | branch
readonly neovim_distros=(
  "default    |false| none                    | none"
  "astro      |false| AstroNvim/template      | default"
  "asyncedd   |false| asyncedd/dots.nvim      | default"
  "barebones  |true | Traap/barebones         | default"
  "barelazy   |true | Traap/barebones         | lazy"
  "baretmux   |true | Traap/barebones         | tmux"
  "cam        |false| ChristianChiarulli/nvim | default"
  "CyberNvim  |false| pgosar/CyberNvim        | default"
  "exos       |false| exosyphon/nvim          | none"
  "kickstart  |false| nvim-lua/kickstart.nvim | default"
  "launch     |false| LunarVim/Launch.nvim    | default"
  "LazyVim    |true | LazyVim/starter         | default"
  "lervag     |false| lervag/dotnvim          | default"
  "NormalNvim |false| NormalNvim/NormalNvim   | default"
  "nvchad     |false| NvChad/starter          | default"
  "nvconf     |false| TechnicalDC/NvConf      | default"
  "OVIwrite   |false| MiragianCycle/OVIWrite  | default"
  "prime      |false| Traap/init.lua          | default"
  "pwnvim     |false| pwnwriter/pwnvim        | default"
  "traap      |true | Traap/nvim              | default"
  "starter    |false| lazyvim/starter         | default"
  "vapour     |false| Traap/VapourNvim        | default"
  "void       |false| nvoid-lua/nvoid         | default"
  "whiskey    |true | Traap/nvim              | 706377a"
  "xray       |true | Traap/nvim              | v0.9.5-lazyvim"
  "zero       |true | Traap/lazy.zero         | default"
  "zulu       |true | Traap/nvim              | v0.6.8-packer"
)
```
Note: see
[neovim_distros](https://github.com/Traap/nvims/blob/master/neovim_distros)
file for latest configuration packages supported and column name discussion.

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
2. nvims remove entries from ```~/.config/nvims/nvim_appnames``` when
   ```nvims -d``` option is used.
3. nvims write ```~/.config/nvims/nvim_default_app``` when ```nvims -s``` option
   is used.
