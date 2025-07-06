#!/bin/sh

export RD="/Applications/Rancher Desktop.app/Contents/Resources/resources/darwin"
export LIMA="/Users/$USER/Library/State/rancher-desktop/lima/rancher-desktop"
export PATH="$RD/lima/bin:$PATH"

qemu-system-x86_64 \
    -cpu Haswell-v4 \
    -machine q35,accel=hvf \
    -smp 2,sockets=1,cores=2,threads=1 \
    -m 4096 \
    -boot order=d,splash-time=0,menu=on \
    -drive file=$LIMA/basedisk,media=cdrom,readonly=on \
    -drive file=$LIMA/diffdisk,if=virtio \
    -cdrom $LIMA/cidata.iso \
    -netdev user,id=net0,net=192.168.5.0/24,dhcpstart=192.168.5.15,hostfwd=tcp:127.0.0.1:63071-:22 \
    -device virtio-net-pci,netdev=net0,mac=52:55:55:66:ca:f6 \
    -device virtio-rng-pci \
    -display cocoa \
    -device virtio-vga \
    -device virtio-keyboard-pci \
    -device virtio-mouse-pci \
    -parallel none \
    -chardev socket,id=char-serial,path=$LIMA/serial.sock,server,nowait,logfile=$LIMA/serial.log \
    -serial chardev:char-serial \
    -chardev socket,id=char-qmp,path=$LIMA/qmp.sock,server,nowait \
    -qmp chardev:char-qmp \
    -name lima-rancher-desktop \
    -pidfile $LIMA/qemu.pid
