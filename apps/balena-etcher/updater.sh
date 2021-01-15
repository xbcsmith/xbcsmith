#!/bin/bash
VERSION="${1:-1.5.106}"
ORG="balena-io"
PROJECT="etcher"
APPNAME="balenaEtcher"
ARCH="x64"
PATH="https://github.com/${ORG}/${PROJECT}/releases/download/v${VERSION}/$APPNAME-${VERSION}-${ARCH}.AppImage"
wget -q --show-progress --progress=bar:force:noscroll
chmod +x $APPNAME-${VERSION}-${ARCH}.AppImage
sed -e "s/@VERSION@/${VERSION}/g" balena.desktop.tmpl > balena.desktop
cp -v balena.desktop ~/.local/share/applications/balena.desktop
