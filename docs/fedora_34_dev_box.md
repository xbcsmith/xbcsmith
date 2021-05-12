# Fedora 34 Development Machine

## Back to VIM

```bash
sudo dnf install vim-default-editor --allowerasing
```

```bash
echo "export EDITOR=$(which vim)" >> .bashrc
```

## Install basics

```bash
sudo dnf install -y \
    rpm-build \
    python3-rpm \
    redhat-rpm-config \
    rpmdevtools \
    fakeroot \
    gcc \
    gcc-c++ \
    clang \
    make \
    cmake \
    vim-enhanced \
    bzip2-devel \
    git \
    hostname \
    openssl \
    openssl-devel \
    sqlite-devel \
    sudo \
    tar \
    wget \
    readline \
    zlib-devel \
    qemu \
    unzip \
    zip \
    p7zip
```

## Install golang

```bash
export GOVERSION=1.16.4
export GOARCH=amd64
curl -kLO https://dl.google.com/go/go${GOVERSION}.linux-${GOARCH}.tar.gz
sudo rm -rfv /usr/local/go
sudo tar -C /usr/local/ -xvzf go${GOVERSION}.linux-${GOARCH}.tar.gz
export PATH=/usr/local/go/bin:$PATH
go version
rm -v go${GOVERSION}.linux-${GOARCH}.tar.gz

mkdir -p ~/go/{src,bin}

cat >> ~/.bashrc << EOF
# GO VARIABLES
export GOPATH=\$HOME/go
export PATH=\$PATH:/usr/local/go/bin:\$GOPATH/bin

EOF

go get -u -v github.com/oklog/ulid/v2/cmd/ulid

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
go get -u -v github.com/go-bindata/go-bindata/...
go get -u -v github.com/josephspurrier/goversioninfo/cmd/goversioninfo
go get -u -v github.com/golang/protobuf/protoc-gen-go

curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.40.0
```

## Install Rust

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

source $HOME/.cargo/env
```

## Install Python Things

```bash
sudo dnf install -y \
    python3-devel \
    python3-pip \
    python3-pyyaml \
    python3-ruamel-yaml \
    python3-ruamel-yaml-clib \
    python3-jinja2  \
    python3-tools  \
    python3-virtualenvwrapper \
    python3-virtualenv \
    python3-pytest \
    python3-tox \
    python3-isort \
    python3-mock \
    black
```

## Install Docker

### Install Upstream

```bash
sudo dnf install -y moby-engine

sudo usermod -aG docker <user>
```

```bash
sudo systemctl enable docker.service

sudo systemctl start docker.service

docker run hello-world
```

## Install Java

```bash
sudo dnf install -y java
```

## NPM

```bash
sudo dnf install nodejs yarnpkg
```

## Git Config

```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
git config --global core.editor vim
git config --global pull.rebase true
```

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

## Linter

```bash
npm install --save --save-exact remark-cli remark-preset-lint-recommended
npm install --save --save-exact markdownlint-cli
npm install --save --save-exact prettier
npm install --save --save-exact @commitlint/cli @commitlint/config-conventional
echo "export PATH=\$PATH:\$HOME/node_modules/.bin" >> ~/.bashrc
echo "module.exports = {extends: ['@commitlint/config-conventional']}" > ~/commitlint.config.js

sudo dnf install -y yamllint ShellCheck hadolint pre-commit
```

## bashrc

Add to the bottom of your .bashrc

```bash
# PYTHON Vars
export PYTHONSTARTUP=~/.pythonrc

source ~/.git-completion.bash

# GRADLE
export GRADLE_USER_HOME=~/.gradle

# JAVA
export JAVA_BIN=$(readlink -f $(which java))
export JAVA_HOME=${JAVA_BIN%%/bin/java}

# GO VARIABLES
export GOPATH=/home/$USER/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN
export PATH=$PATH:/usr/local/bin/go/bin

# RUST
export CARGOBIN=/home/bsmith/.cargo/bin
export PATH=$PATH:$CARGOBIN

# SNAPD
export PATH=$PATH:/home/bsmith/snap/bin

# NPM
export PATH=$PATH:/home/bsmith/node_modules/.bin
```

## pythonrc

Add a .pythonrc

```bash
cat > .pythonrc << EOF
# enable syntax completion
try:
    import readline
except ImportError:
    print("Module readline not available.")
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")

EOF
```

## Python Virtual env

```bash
mkdir -p ~/.virtualenvs
/usr/bin/python3 -m venv ~/.virtualenvs/foo
source ~/.virtualenvs/foo/bin/activate

pip install --upgrade pip setuptools pbr six setuptools wheel
pip install --upgrade rfc3987 PyYAML stevedore jsonschema Jinja2  docker
pip install --upgrade autopep8 flake8 tox black isort pdbpp
```

## Python format script

```bash
cat > ~/bin/format_python << EOF
#!/bin/bash
isort --atomic "${@}"
black --line-length=120 "${@}"
flake8 --max-line-length=120 "${@}"

EOF

chmod +x ~/bin/format_python
```

## Nautilus

Edit default folders

```bash
sudo vim /etc/xdg/user-dirs.defaults
```

```bash
vim ~/.config/user-dirs.dirs
rm -rf Downloads/ Music/ Public/ Templates/ Videos/ Pictures/ Desktop/ Documents/
mkdir ~/downloads
```

or

```bash
sudo echo -en "DOWNLOAD=downloads\n" > /etc/xdg/user-dirs.defaults
echo -en "DOWNLOAD=downloads\n" > ~/.config/user-dirs.dirs
rm -rf Downloads/ Music/ Public/ Templates/ Videos/ Pictures/ Desktop/ Documents/
mkdir -p ~/downloads
```

## Atom IDE

```bash
sudo rpm --import https://packagecloud.io/AtomEditor/atom/gpgkey
sudo sh -c 'echo -e "[Atom]\nname=Atom Editor\nbaseurl=https://packagecloud.io/AtomEditor/atom/el/7/\$basearch\nenabled=1\ngpgcheck=0\nrepo_gpgcheck=1\ngpgkey=https://packagecloud.io/AtomEditor/atom/gpgkey" > /etc/yum.repos.d/atom.repo'
sudo dnf install atom
```

## ImageMagick with heic

```bash
sudo dnf remove ImageMagick
sudo dnf install libheif libheif-devel libjpeg libjpeg-devel
cd /tmp
git clone https://github.com/ImageMagick/ImageMagick.git
cd ./ImageMagick
./configure --with-heic --with-jpeg
make -j4
make install
sudo make install
sudo ldconfig
cd ..
rm -rf ImageMagick
```

## Desktop

gnome tweaks

```bash
sudo dnf install gnome-tweak-tool
```

gimp and friends

```bash
sudo dnf install gimp inkscape dia terminator
```

rpmfusion

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

VSCodium

```bash
https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo
```

VNC

Install VNC Server.

```bash
sudo dnf -y install tigervnc-server
```

If Firewalld is running, allow VNC service.

```bash
sudo firewall-cmd --add-service=vnc-server --permanent
sudo firewall-cmd --reload
```

Login as a user you would like to configure VNC session.

set VNC password

```bash
vncpasswd
```

edit your config

```bash
vi ~/.vnc/config
```

```text
# create new

# session=(display manager you use)

# securitytypes=(security options)

# geometry=(screen resolution)

session=gnome
securitytypes=vncauth,tlsvnc
geometry==1600x1200
```

Configure settings with root privilege ans start Systemd Unit.

```bash
vi /etc/tigervnc/vncserver.users
```

```text
# add to the end

# specify [:(display number)=(username] as comments

# display number 1 listens port 5901

# display number n + 5900 = listening port

#
# This file assigns users to specific VNC display numbers.
# The syntax is <display>=<username>. E.g.:
#
# :2=andrew
# :3=lisa
:1=fedora
:2=redhat

# start systemd unit
```

Enable and start vnc

```bash
systemctl enable --now vncserver@:1 vncserver@:2
```

Login using \<hostname\>:5901

P0l4r!s
