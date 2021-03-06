# Mac OS X Dev Machine

## Firefox

<https://www.mozilla.org/en-US/firefox/new>

## Xcode

App Store

## Atom

<https://atom.io>

## Keka

<https://www.keka.io/en>

## Docker Desktop

<https://download.docker.com/mac/stable/Docker.dmg>

## Insync

<https://www.insynchq.com/downloads>

## Iterm2

<https://www.iterm2.com/downloads.html>

<https://www.iterm2.com/documentation-status-bar.html>

## Fonts

```bash
defaults -currentHost write -globalDomain AppleFontSmoothing -int 3
```

## Brew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

## Bash 5

```bash
brew install bash bash-completion
which -a bash
/usr/local/bin/bash --version
sudo vim /etc/shells
chsh -s /usr/local/bin/bash
```

## Core Utils

```bash
brew install coreutils findutils gnu-tar gnu-sed gawk gnutls gnu-indent \
  gnu-getopt grep gnutls
```

```bash
PATHS=$(brew info coreutils findutils gnu-tar gnu-sed gawk gnutls gnu-indent | grep PATH=)
for path in $PATHS;do
    echo "export $path";
done
```

Add output to bashrc

```bash
# GNU Paths
export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/findutils/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/gnu-tar/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/gnu-sed/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/gnu-indent/libexec/gnubin:$PATH"
```

## Cloud

```bash
brew install kubectl kind minikube minishift
```

```bash
brew tap argoproj/tap
brew install argoproj/tap/argocd
brew install argoproj/tap/argo
```

## Vim

**brings** in a lot of things

```bash
brew install vim
```

<https://github.com/macvim-dev/macvim/releases>

## Git

```bash
brew install git
```

## Git Config

```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
git config --global core.editor vim
git config --global pull.rebase true
```

## Git Aliases

```bash
git config --global alias.st status
git config --global alias.last "log -1 HEAD"
git config --global alias.br "branch -r"
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.unstage "reset HEAD --"
git config --global alias.b branch
git config --global alias.t "tag --list -n"
git config --global alias.cb "checkout -b"
git config --global alias.can "commit --amend --no-edit"
git config --global alias.lt "describe --tags"
git config --global alias.pl "pull --rebase --autostash"
```

## Python

probably already installed by **vim**

```bash
brew install python3
```

```bash
syspip3 install virtualenv virtualenvwrapper

source /usr/local/bin/virtualenvwrapper_lazy.sh
mkvirtualenv --python $(which python3) foo

pip install --upgrade pip setuptools pbr wheel
pip install --upgrade rfc3987 enum34 PyYAML stevedore jsonschema Jinja2
pip install --upgrade autopep8 flake8 tox pdbpp isort black mock tox
pip install --upgrade docker reuse
```

## Go and Rust

```bash
brew install go rust
```

```bash
brew install golangci/tap/golangci-lint
brew upgrade golangci/tap/golangci-lint

go get -u -v golang.org/x/tools/...
go get -u -v golang.org/x/tools/cmd/goimports
go get -u -v golang.org/x/lint/golint
go get -u -v github.com/fzipp/gocyclo
go get -u -v github.com/uudashr/gocognit/cmd/gocognit
go get -u -v github.com/go-critic/go-critic/cmd/gocritic
go get -u -v github.com/wadey/gocovmerge
go get -u -v github.com/axw/gocov/gocov
go get -u -v github.com/AlekSi/gocov-xml
go get -u -v github.com/tebeka/go2xunit
go get -u -v github.com/shuLhan/go-bindata/cmd/go-bindata
go get -u -v github.com/josephspurrier/goversioninfo/cmd/goversioninfo
go get -u -v github.com/golang/protobuf/protoc-gen-go
```

## Node

```bash
brew install node
```

add to bashrc

```bash
# Node PATH
export PATH="$PATH:/Users/bsmith/node_modules/.bin"
```

## Lint

```bash
npm install markdownlint-cli
npm install commitlint
echo "module.exports = {extends: ['@commitlint/config-conventional']}" > /commitlint.config.js
```

## Misc

```bash
brew cask install macdown vscodium

brew install tree xz yamllint wget

brew install pwgen pyenv pyenv-virtualenv pyenv-virtualenvwrapper \
    kafkacat jq gnutls
```
