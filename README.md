# ansible-role-cmd-utils

This ansible role installs and configures a lot of useful command line
tools. The configurations are highly customized und mainly fit to my
purposes. Feel free to adapt it to your needs.

## Utilities

The following software packages are installed and configured:

- `zsh`: **The** shell for unix-like systems
- `oh-my-zsh`: Collection of useful tools and configurations around `zsh`
- `tmux`: My favourite terminal multiplexer
- `git`: Configures git and sets some life-changing aliases
- `fzf`: A Fuzzy command line search
- `jrnl`: Command line journaling tool
- `virtualenvwrapper`: Python library to wrap environments

## Gadets

### tmux and ssh

This role takes care that `ssh-agent` is registered with your private
key in all panes and windows of your tmux session.

### tmux and vim

`tmux` is configured to work together with my VIM setup (see
[here](https://github.com/windisch/vim))

### zsh

The `z`-shell is installed and selected to be the default shell. Then,
[`oh-my-zsh`](http://github.com/robbyrussel/oh-my-zsh), a collection
of useful `zsh` tools and sane configurations, is cloned and sourced.
Here, the `vim` bindings are enabled.

### fzf

The [fuzzy command line finder](https://github.com/junegunn/fzf.git)
is installed and some aliases are set. It can be used to search the
shell history, git branches and commits, files, and many more.
Unfortuantely, pre-build binaries for `fzf` are not available for many
platforms. Hence, it cloned and installed from
`https://github.com/junegunn/fzf.git`.

### Python
The python packages `virtualenv` and `virtualenvwrapper` are installed
(via `pip`) and ensured to be loaded uppon a start of the `z`-shell.
The interactive python shell `ipython` is installed and some startup
scripts are placed.

## Requirements

Along the provisioning, the following packages are installed using the
package manager of your system (make sure that these are availabe):
`go` (`golang` under debian based systems), `zsh`, `tmux`.

Moreover, pythons package manager `pip` is assumed to be available.

## Shortcuts

- `CTRL-R`: Search command history with `fzf`
- `ESC-v`: Edit current command with `vim` 

## Aliases

- `gitcm`: Short for `git commit -m`
- `gitv`: Shows commit tree of `git`
- `fgit`: Fuzzy search of branches in `git` repository
- `fgita`: Fuzzy search of changed files in `git` repository
- `fjrln`: Fuzzy search of `jrnl` entry headlines
- `fkill`: Fuzzy search of processes. Selected process gets killed.
- `p`: Short for `python`
- `wo`: Short for VirtualEnv command `workon`
