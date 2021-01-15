#!/bin/bash
VERSION="${1:-4.0.6}"
PATH="https://github.com/lensapp/lens/releases/download/v${VERSION}/Lens-${VERSION}.AppImage"
wget -q --show-progress --progress=bar:force:noscroll ${PATH}
chmod +x Lens-${VERSION}-x64.AppImage
sed -e "s/@VERSION@/${VERSION}/g" lens.desktop.tmpl > lens.desktop
cp -v lens.desktop ~/.local/share/applications/lens.desktop
