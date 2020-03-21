# Ubuntu 18.04 Dev Machine

## EDITOR

_Always **vim**_

```bash
sudo update-alternatives --config editor
```

## GO

```bash
sudo add-apt-repository ppa:longsleep/golang-backports
sudo apt-get update
sudo apt-get install golang-go
```

## Rust

```bash
sudo apt-get install rustc cargo dh-cargo
```

## Docker

```bash
sudo apt-get remove docker docker-engine docker.io
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) edge"
sudo apt-get update
sudo apt-get install docker-ce
```

### Expose port to world... seems safe

Actually if you do this you should secure it.

```bash
mkdir /etc/docker
cat > /etc/docker/daemon.json << EOF
{
"debug": true,
"hosts": ["tcp://0.0.0.0:2375", "unix:///var/run/docker.sock"]
}

EOF

sed -i 's~dockerd -H fd://~dockerd~g' /lib/systemd/system/docker.service
sudo sed -i 's~StartLimitInterval=60s~StartLimitInterval=60s\nIPForward=yes\n~g' /lib/systemd/system/docker.service
```

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
sudo usermod -aG sudo $USER
sudo systemctl enable docker
sudo systemctl start docker
```

```bash
docker run --rm -it hello-world
```

## Devel Pkgs

```bash
sudo apt-get -y update && sudo apt-get -y install build-essential devscripts fakeroot debhelper dpkg-dev automake autotools-dev autoconf libtool perl libperl-dev systemtap-sdt-dev libssl-dev python-dev python3-dev m4 bison flex docbook-dsssl docbook-xml docbook-xsl docbook opensp xsltproc gettext unzip wget libguestfs-tools virtualenvwrapper tox python3-virtualenv openjdk-8-jre-headless openjdk-8-jdk-headless pkg-config python-logilab-common python-unittest2 python-mock zip
sudo apt-get -y install python-autopep8 python3-flake8 flake8 python-flake8 isort python-isort python3-isort vim-autopep8 python-wheel python3-wheel python-pip python3-pip tox
```

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6 python3.6-venv python3.7 python3.7-venv
```

## Virtual Env

```bash
mkdir -p ~/.virtualenvs
PYTHON3=$(which python3.7)
$PYTHON3 -m venv ~/.virtualenvs/foo
source ~/.virtualenvs/foo/bin/activate

pip install --upgrade pip setuptools pbr wheel pip pkg_resources functools32 docker
pip install --upgrade rfc3987 enum34 PyYAML stevedore jsonschema Jinja2
pip install --upgrade autopep8 flake8 tox black isort pdbpp
```

## NPM

```bash
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key add -
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt install nodejs yarn
```
