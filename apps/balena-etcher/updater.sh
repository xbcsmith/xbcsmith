#!/usr/bin/env bash

VERSION="${1:-1.5.106}"
ORG="balena-io"
PROJECT="etcher"
APPNAME="balenaEtcher"
ARCH="x64"
BINARY="https://github.com/${ORG}/${PROJECT}/releases/download/v${VERSION}/${APPNAME}-${VERSION}-${ARCH}.AppImage"

echo "updating ${APPNAME} to ${VERSION} ${BINARY}"

wget -O ${APPNAME}-${VERSION}-${ARCH}.AppImage --show-progress --progress=bar:force:noscroll ${BINARY}
chmod +x ${APPNAME}-${VERSION}-${ARCH}.AppImage
sed -e "s/@VERSION@/${VERSION}/g" ${APPNAME,,}.desktop.tmpl > ${APPNAME,,}.desktop
cp -v ${APPNAME,,}.desktop ~/.local/share/applications/${APPNAME,,}.desktop
