# Single User TightVNC Server setup

## Install GNOME

### CentOS 7 & 8 Gnome

```bash
sudo yum groupinstall "GNOME Desktop" "Graphical Administration Tools"
```

### Fedora 31 Gnome

```bash
dnf -y group install "Basic Desktop" GNOME
```

## Install TigerVNC

### CentOS 7 & 8 TigerVNC

```bash
sudo yum install tigervnc-server
```

### Fedora 31 TigerVNC

```bash
sudo dnf install tigervnc-server
```

At this point I rebooted...

```bash
sudo shutdown -r now
```

## Configure

```bash
mkdir ~/.vnc
```

```bash
vncpasswd
```

Type Password

```bash
Password:
Verify:
Would you like to enter a view-only password (y/n)? n
A view-only password is not used
```

```bash
cat > .vnc/xstartup << EOF
#!/bin/sh
# Add the following line to ensure you always have an xterm available.
#( while true ; do xterm ; done ) &
# Uncomment the following two lines for normal desktop:
unset SESSION_MANAGER
. /etc/X11/xinit/xinitrc

[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey
vncconfig -iconic &
x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &

EOF

chmod +x .vnc/xstartup
```

```bash
cat > ~/bin/startvnc << EOF
vncserver :5901 -geometry 1280x960 -depth 24

EOF

chmod +x bin/startvnc
```

```bash
cat > ~/bin/stopvnc << EOF
#!/bin/bash

vncserver -kill :5901

EOF

chmod +x bin/stopvnc
```

Make sure firewall is allowing connections. (Google opening ports in firewall if
you need to fix it)

```bash
sudo iptables -L
```

## Start VNC

```bash
ssh bsmith@xbcsmith.foo.com

startvnc
```

```bash
New 'bsmith@xbcsmith.foo.com:5901 (bsmith)' desktop is bsmith@xbcsmith.foo.com:5901

Starting applications specified in /home/bsmith/.vnc/xstartup
Log file is /home/bsmith/.vnc/bsmith@xbcsmith.foo.com:5901.log
```

## From another machine connect

```bash
vncviewer xbcsmith.foo.com:5901
```
