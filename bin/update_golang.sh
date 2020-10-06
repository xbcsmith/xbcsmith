#!/usr/bin/env bash

export GOVERSION=${GOVERSION:-$1}

cd

OS=$(uname)
ARCH=$(arch)
case $ARCH in
  "aarch64" ) export GOARCH=arm64
          ;;
  "x86_64" ) export GOARCH=amd64
          ;;
         * ) export GOARCH=$(go env GOARCH)
          ;;
esac

echo "Updating to Go ${GOVERSION} ${GOARCH}"

curl -kLO https://dl.google.com/go/go${GOVERSION}.${OS,,}-${GOARCH}.tar.gz
sudo rm -rfv /usr/local/go
sudo tar -C /usr/local/ -xvzf go${GOVERSION}.${OS,,}-${GOARCH}.tar.gz
export PATH=/usr/local/go/bin:$PATH
go version
rm -v go${GOVERSION}.${OS,,}-${GOARCH}.tar.gz
