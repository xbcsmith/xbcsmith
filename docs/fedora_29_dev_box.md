# Fedora 29 Development Machine

## Install basics

```bash
sudo dnf install -y \
    rpm-build \
    rpm-python \
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
sudo dnf install -y golang
mkdir -p ~/go/{src,bin}
```

## Install Rust

```bash
sudo dnf install -y rust cargo
```

## Install Python Things

```bash
sudo dnf install -y PyYAML \
    python-devel \
    python-tools \
    python-jinja2  \
    python-pip \
    python-virtualenvwrapper \
    python-virtualenv \
    python-pytest \
    python-mock \
    python3-devel \
    python3-pip \
    python3-jinja2  \
    python3-tools  \
    python3-virtualenvwrapper \
    python3-virtualenv \
    python3-pytest \
    python3-tox \
    python3-mock
```

## Install Docker

### Create a partition (optional)

```bash
lsblk
df -Th
swapoff /dev/mapper/fedora-swap
pvdisplay
lvdisplay
lvcreate -L75GB -n docker fedora
lsblk
mkdir /var/lib/docker
mkfs.ext4 /dev/mapper/fedora-docker
echo "/dev/mapper/fedora-docker /var/lib/docker       ext4    defaults        0 0" >> /etc/fstab
mount /var/lib/docker/
```

### Remove old dockers

```bash
sudo dnf remove -y docker \
    docker-client \
    docker-client-latest \
    docker-common \
    docker-latest \
    docker-latest-logrotate \
    docker-logrotate \
    docker-selinux \
    docker-engine-selinux \
    docker-engine
```

### Install Upstream

```bash
sudo dnf -y install dnf-plugins-core

sudo dnf config-manager \
    --add-repo \
    https://download.docker.com/linux/fedora/docker-ce.repo

sudo dnf config-manager --set-enabled docker-ce-edge

sudo dnf install -y docker-ce

sudo usermod -aG docker <user>

sudo su -

mkdir /etc/docker

cat > /etc/docker/daemon.json << EOF
{
"debug": true,
"hosts": ["tcp://0.0.0.0:2375", "unix:///var/run/docker.sock"]
}


EOF

sed -i 's~dockerd -H fd://~dockerd~g' /lib/systemd/system/docker.service

systemctl enable docker.service
systemctl start docker.service

docker run hello-world
```

## Install Java

```bash
sudo dnf install -y java-1.8.0-openjdk-devel \
    java-11-openjdk-devel \
    java-10-openjdk-devel
```

## Add to the bottom of your .bashrc

```bash
# PYTHON Vars
export PYTHONSTARTUP=~/.pythonrc

source ~/.git-completion.bash
source ~/.screen-completion.bash

# GRADLE
export GRADLE_USER_HOME=~/.gradle

# JAVA
export JAVA_BIN=$(readlink -f $(which java))
export JAVA_HOME=${JAVA_BIN%%/bin/java}

# GO VARIABLES
export GOPATH=/home/bsmith/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN
```

## Add a .pythonrc

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
