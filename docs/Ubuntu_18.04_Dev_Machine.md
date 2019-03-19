# Ubuntu 18.04 Dev Machine


## EDITOR

### Always vim

```
sudo update-alternatives --config editor
```

## GO

```
sudo add-apt-repository ppa:gophers/archive
sudo apt-get update
sudo apt-get install golang-1.10-go
```

## Docker 

```
sudo apt-get remove docker docker-engine docker.io
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) edge"
sudo apt-get update
sudo apt-get install docker-ce
```

### Expose port to world... seems safe

```
sudo sed -i 's~-H fd://~-H fd:// -H tcp://0.0.0.0:2375~g' /lib/systemd/system/docker.service
sudo sed -i 's~StartLimitInterval=60s~StartLimitInterval=60s\nIPForward=yes\n~g' /lib/systemd/system/docker.service
```


```
sudo groupadd docker
sudo usermod -aG docker $USER
sudo usermod -aG sudo $USER
sudo systemctl enable docker
sudo systemctl start docker
```

```
docker run --rm -it aarch64/hello-world
```

## Devel Pkgs

```
sudo apt-get -y update && sudo apt-get -y install build-essential devscripts fakeroot debhelper dpkg-dev automake autotools-dev autoconf libtool perl libperl-dev systemtap-sdt-dev libssl-dev python-dev python3-dev m4 bison flex docbook-dsssl docbook-xml docbook-xsl docbook opensp xsltproc gettext unzip wget libguestfs-tools virtualenvwrapper tox python3-virtualenv openjdk-8-jre-headless openjdk-8-jdk-headless pkg-config python-logilab-common python-unittest2 python-mock zip
sudo apt-get -y install python-autopep8 python3-flake8 flake8 python-flake8 isort python-isort python3-isort vim-autopep8 python-wheel python3-wheel python-pip python3-pip tox 
```

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.5 python3.4
```


## Virtual Env


```
mkvirtualenv foo
pip install --upgrade pip setuptools pbr wheel pip pkg_resources functools32 docker
pip install --upgrade rfc3987 enum34 PyYAML stevedore jsonschema Jinja2
pip install --upgrade autopep8 flake8 tox black isort pdbpp
```


