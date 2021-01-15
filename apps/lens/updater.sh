#!/usr/bin/env bash
set -x
VERSION="${1:-4.0.6}"
ORG="lensapp"
PROJECT="lens"
APPNAME="Lens"
ARCH="x64"
BINARY="https://github.com/${ORG}/${PROJECT}/releases/download/v${VERSION}/${APPNAME}-${VERSION}.AppImage"

echo "updating ${APPNAME} to ${VERSION} ${BINARY}"

wget -O ${APPNAME}-${VERSION}-${ARCH}.AppImage --show-progress --progress=bar:force:noscroll ${BINARY}
chmod +x ${APPNAME}-${VERSION}-${ARCH}.AppImage
sed -e "s/@VERSION@/${VERSION}/g" ${APPNAME,,}.desktop.tmpl > ${APPNAME,,}.desktop
cp -v ${APPNAME,,}.desktop ~/.local/share/applications/${APPNAME,,}.desktop
