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

go get -u golang.org/x/tools/...
go get -u golang.org/x/lint/golint

go get -v github.com/go-lintpack/lintpack/...
go get -v github.com/go-critic/go-critic/...
cd $(go env GOPATH)/src/github.com/go-critic/go-critic && make gocritic \
  && mv -v gocritic $GOPATH/bin/
```

## Node

```bash
brew install node
npm install -g markdownlint-cli
```

add to bashrc

```bash
# Node PATH
export PATH="$PATH:/Users/bsmith/node_modules/.bin"
```

## Misc

```bash
brew cask install macdown vscodium

brew install tree xz yamllint wget

brew install pwgen pyenv pyenv-virtualenv pyenv-virtualenvwrapper \
    kafkacat jq gnutls
```
