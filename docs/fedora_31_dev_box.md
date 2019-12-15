# Fedora 29 Development Machine

## Install basics

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

## Install golang

    sudo dnf install -y snapd

## Install Rust

    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

    source $HOME/.cargo/env

##  Install Python Things

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

## Install Docker


### Create a partition (optional)

    lsblk
    df -Th
    swapoff /dev/mapper/fedora-swap
    pvdisplay
    lvdisplay
    lvcreate -L75GB -n docker fedora
    lsblk
    mkdir /var/lib/docker
    mkfs.ext4 /dev/mapper/fedora-docker
    echo "/dev/mapper/fedora-docker /var/lib/docker       ext4	defaults        0 0" >> /etc/fstab
    mount /var/lib/docker/

### Temporary workaround CgroupsV2


    sudo vim /etc/default/grub

Append value of GRUB_CMDLINE_LINUX with systemd.unified_cgroup_hierarchy=0

    sudo grub2-mkconfig > /boot/efi/EFI/fedora/grub.cfg

or

    sudo grub2-mkconfig > /boot/grub2/grub.cfg

    reboot


### Install Upstream

    sudo dnf install -y moby-engine

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

## Install Java

    sudo dnf install -y java 

## Add to the bottom of your .bashrc

```
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



