# Fedora 42 Development Machine

## Enable SSH access

```bash
rpm -qa | grep openssh-server
```

If openssh is not installed:

```bash
sudo dnf install openssh-server
```

```bash
sudo systemctl enable sshd
sudo systemctl start sshd
sudo systemctl status sshd
sudo ss -lt
```

## Back to VIM

```bash
sudo dnf install vim-default-editor --allowerasing
```

```bash
echo "export EDITOR=$(which vim)" >> .bashrc
```

## Headless

```bash
sudo systemctl get-default
sudo systemctl set-default multi-user.target
```

## Updates

```bash
sudo dnf update
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
export GOVERSION=1.25.1
export GOARCH=amd64
export GOOS=linux
export GO_CHECKSUM=7716a0d940a0f6ae8e1f3b3f4f36299dc53e31b16840dbd171254312c41ca12e
curl -kLO https://dl.google.com/go/go${GOVERSION}.${GOOS}-${GOARCH}.tar.gz
echo "${GO_CHECKSUM} go${GOVERSION}.${GOOS}-${GOARCH}.tar.gz" | sha256sum --check
sudo rm -rfv /usr/local/go
sudo tar -C /usr/local/ -xvzf go${GOVERSION}.${GOOS}-${GOARCH}.tar.gz
export PATH=/usr/local/go/bin:$PATH
go version
rm -v go${GOVERSION}.${GOOS}-${GOARCH}.tar.gz
```

## Setup Go Tools

```bash
mkdir -p ~/go/{src,bin}

cat >> ~/.bashrc << EOF
# GO VARIABLES
export GOPATH=\$HOME/go
export PATH=\$PATH:/usr/local/go/bin:\$GOPATH/bin

EOF

go install github.com/go-delve/delve/cmd/dlv@latest
go install github.com/oklog/ulid/v2/cmd/ulid@latest


go install golang.org/x/tools/...@latest
go install github.com/AlekSi/gocov-xml@latest
go install github.com/axw/gocov/gocov@latest
go install github.com/golang/protobuf/protoc-gen-go@latest
go install github.com/josephspurrier/goversioninfo/cmd/goversioninfo@latest
go install github.com/tebeka/go2xunit@latest
go install github.com/wadey/gocovmerge@latest
go install golang.org/x/tools/cmd/goimports@latest
go install golang.org/x/tools/gopls@latest



export GOLANGCI_LINT_VERSION="2.4.0"
curl -sSfL https://github.com/golangci/golangci-lint/releases/download/v${GOLANGCI_LINT_VERSION}/golangci-lint-${GOLANGCI_LINT_VERSION}-linux-amd64.tar.gz -o golangci-lint-${GOLANGCI_LINT_VERSION}-linux-amd64.tar.gz
curl -sSfL https://github.com/golangci/golangci-lint/releases/download/v${GOLANGCI_LINT_VERSION}/golangci-lint-${GOLANGCI_LINT_VERSION}-checksums.txt | grep linux-amd64.tar.gz | sha256sum --check
tar -C $(go env GOPATH)/bin -xvzf golangci-lint-${GOLANGCI_LINT_VERSION}-linux-amd64.tar.gz golangci-lint-${GOLANGCI_LINT_VERSION}-linux-amd64/golangci-lint --strip-components 1
rm -vf golangci-lint-${GOLANGCI_LINT_VERSION}-linux-amd64.tar.gz
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
    ruff
```

## Install Docker

### Install Upstream

```bash
sudo dnf install -y moby-engine

sudo usermod -aG docker ${USER}
```

Enable and Start

```bash
sudo systemctl enable docker.service

sudo systemctl start docker.service

docker run hello-world
```

Grab some more tools

```bash
sudo dnf install -y podman buildah
```

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"

echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check  && \
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

```bash
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64 && \
echo "cddeab5ab86ab98e4900afac9d62384dae0941498dfbe712ae0c8868250bc3d7  minikube-linux-amd64" | sha256sum --check  && \
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

```bash
go install sigs.k8s.io/kind@v0.30.0
```

## Install Java

```bash
sudo dnf install -y java
```

## NPM

```bash
sudo dnf install -y nodejs yarnpkg
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

export PATH=$PATH:$HOME/bin

# GO VARIABLES
export GOPATH=/home/$USER/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN
export PATH=$PATH:/usr/local/go/bin

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

pip install --upgrade pip setuptools setuptools wheel poetry
pip install --upgrade rfc3987 PyYAML stevedore jsonschema Jinja2  docker
pip install --upgrade ruff tox pdbpp
```

## Format Scripts

### Python

```bash
cat > ~/bin/format_python << EOF
#!/bin/bash

for FILE in $@;do
    filename="$(basename $FILE)"
    if [[ $FILE =~ \.py$ ]];then
        echo "Formatting : ${filename}"
        isort --atomic --profile black "${FILE}"
        black --line-length=120 "${FILE}"
        flake8 --max-line-length=120 "${FILE}"
    else
        echo "Skipping : ${filename} is NOT a python file"
    fi
done

EOF

chmod +x ~/bin/format_python
```

### Markdown

```bash
cat > ~/bin/format_markdown << EOF
#!/usr/bin/env bash

for FILE in $@;do
    filename="$(basename $FILE)"
    if [[ $FILE =~ \.md$ ]];then
        echo "Formatting : ${filename}"
        prettier --write --parser markdown --prose-wrap always "${FILE}"
    else
        echo "Skipping : ${filename} is NOT a markdown file"
    fi
done

EOF

chmod +x ~/bin/format_markdown
```

### YAML

```bash
cat > ~/bin/format_yaml << EOF
#!/usr/bin/env bash

for FILE in $@;do
    filename="$(basename $FILE)"
    if [[ $FILE =~ \.yaml$ ]] || [[ $FILE =~ \.yml$ ]];then
        echo "Formatting : ${filename}"
        prettier --write "${FILE}"
    else
        echo "Skipping : ${filename} is NOT a yaml file"
    fi
done

EOF

chmod +x ~/bin/format_yaml
```

## Add New User

```bash
export NEW_USER="foo"
sudo groupadd ${NEW_USER}
sudo useradd -m -g ${NEW_USER} -G wheel,docker -s /bin/bash -d /home/${NEW_USER} ${NEW_USER}
echo 'ChangeME!' | sudo passwd ${NEW_USER} --stdin
```

```bash
USERS="joe strummer foo"
for U in $USERS;do
  sudo groupadd ${U}
  sudo useradd -m -g ${U} -G wheel,docker -s /bin/bash -d /home/${U} ${U}
  echo 'P0l4r1s_!' | sudo passwd ${U} --stdin
done
```

## Desktop

### Customize Nautilus

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
sudo su -c echo -en "DOWNLOAD=downloads\n" > /etc/xdg/user-dirs.defaults
echo -en "DOWNLOAD=downloads\n" > ~/.config/user-dirs.dirs
rm -rf Downloads/ Music/ Public/ Templates/ Videos/ Pictures/ Desktop/ Documents/
mkdir -p ~/downloads
```

### Install Nice to Have

Install gnome tweaks

```bash
sudo dnf install -y gnome-tweak-tool
```

Install graphics tools and terminal

```bash
sudo dnf install -y gimp inkscape dia terminator
```

If running as a VM on VMWare

```bash
sudo dnf install -y open-vm-tools open-vm-tools-desktop
```

## ImageMagick with heic

```bash
sudo dnf remove ImageMagick
sudo dnf install -y libheif libheif-devel libjpeg libjpeg-devel
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

### Add rpmfusion repos

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

### Install VSCodium

```bash
https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo
```

```bash
sudo tee -a /etc/yum.repos.d/vscodium.repo << 'EOF'
[gitlab.com_paulcarroty_vscodium_repo]
name=gitlab.com_paulcarroty_vscodium_repo
baseurl=https://paulcarroty.gitlab.io/vscodium-deb-rpm-repo/rpms/
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg
metadata_expire=1h
EOF

```

```bash
sudo dnf install -y codium
```

### VSCode

Or you can install the actual VSCode.

```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo dnf install -y code
```

### Setup VNC

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
geometry=1600x1200
```

Configure settings with root privilege ans start Systemd Unit.

```bash
sudo vim /etc/tigervnc/vncserver.users
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
sudo systemctl enable --now vncserver@:1 vncserver@:2
```

Login using \<hostname\>:5901

### PCSD Socket problem work around

```bash
sudo systemctl stop pcscd.socket
sudo systemctl stop pcscd
sudo systemctl disable pcscd.socket
sudo systemctl disable pcscd.service
```

## Disable WIFI Power Saver

```bash
sudo tee /etc/NetworkManager/conf.d/00-wifi-powersave.conf << EOF > /dev/null
[connection]
wifi.powersave=2

EOF

sudo systemctl restart NetworkManager.service
```
