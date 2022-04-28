# Mac OS X Dev Machine

## Firefox

<https://www.mozilla.org/en-US/firefox/new>

## Xcode

App Store

## Atom

<https://atom.io>

## Keka

<https://www.keka.io/en>

## Rancher Desktop

<https://rancherdesktop.io/>

## Insync

<https://www.insynchq.com/downloads>

## Iterm2

<https://www.iterm2.com/downloads.html>

<https://www.iterm2.com/documentation-status-bar.html>

## Fonts

```bash
defaults -currentHost write -globalDomain AppleFontSmoothing -int 3
```

## Brew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/${USER}/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

## Bash 5

```bash
brew install bash bash-completion
which -a bash
/opt/homebrew/bin/bash --version
sudo vim /etc/shells
chsh -s /opt/homebrew/bin/bash
```

Add the following to `~/.bashrc`

```bash
export PATH="/opt/homebrew/bin:$PATH"
[[ -r "/opt/homebrew/etc/profile.d/bash_completion.sh" ]] && . "/opt/homebrew/etc/profile.d/bash_completion.sh"
```

## Core Utils

```bash
brew install coreutils findutils gnu-tar gnu-sed gawk gnutls gnu-indent gnu-getopt grep gnutls
```

```bash
PATHS=$(brew info coreutils findutils gnu-tar gnu-sed gawk gnutls gnu-indent | grep PATH=)
for path in $PATHS;do
    echo "export $path";
done
```

Add output to bashrc

```bash
# GNU Paths
export PATH="/opt/homebrew/opt/coreutils/libexec/gnubin:$PATH"
export PATH="/opt/homebrew/opt/findutils/libexec/gnubin:$PATH"
export PATH="/opt/homebrew/opt/gnu-tar/libexec/gnubin:$PATH"
export PATH="/opt/homebrew/opt/gnu-sed/libexec/gnubin:$PATH"
export PATH="/opt/homebrew/opt/gnu-indent/libexec/gnubin:$PATH"
```

## Cloud

```bash
brew install kubectl kind minikube minishift
```

```bash
brew tap argoproj/tap
brew install argoproj/tap/argocd
brew install argoproj/tap/argo
```

## Vim

**brings** in a lot of things

```bash
brew install vim
```

<https://github.com/macvim-dev/macvim/releases>

## Git

```bash
brew install git
```

## Git Config

```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
git config --global core.editor vim
git config --global pull.rebase true
```

## Git Aliases

```bash
git config --global alias.st status
git config --global alias.last "log -1 HEAD"
git config --global alias.br "branch -r"
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.unstage "reset HEAD --"
git config --global alias.b branch
git config --global alias.t "tag --list -n"
git config --global alias.cb "checkout -b"
git config --global alias.can "commit --amend --no-edit"
git config --global alias.lt "describe --tags"
git config --global alias.pl "pull --rebase --autostash"
```

## Python

probably already installed by **vim**

```bash
brew install python3
```

```bash
brew install virtualenv virtualenvwrapper pyenv

source /opt/homebrew/bin/virtualenvwrapper_lazy.sh
mkvirtualenv --python $(which python3) foo

pip3 install --upgrade pip setuptools pbr wheel
pip3 install --upgrade rfc3987 enum34 PyYAML stevedore jsonschema Jinja2
pip3 install --upgrade flake8 tox pdbpp isort black mock tox
pip3 install --upgrade docker reuse pre-commit yamllint
```

## Go and Rust

```bash
brew install go rust
```

```bash
brew install golangci/tap/golangci-lint
brew upgrade golangci/tap/golangci-lint

go install golang.org/x/tools/...@latest
go install golang.org/x/tools/cmd/goimports@latest
go install github.com/fzipp/gocyclo/cmd/gocyclo@latest
go install github.com/uudashr/gocognit/cmd/gocognit@latest
go install github.com/go-critic/go-critic/cmd/gocritic@latest
go install github.com/wadey/gocovmerge@latest
go install github.com/axw/gocov/gocov@latest
go install github.com/AlekSi/gocov-xml@latest
go install github.com/tebeka/go2xunit@latest
go install github.com/josephspurrier/goversioninfo/cmd/goversioninfo@latest
go install github.com/golang/protobuf/protoc-gen-go@latest
```

## Node

```bash
brew install node
```

add to bashrc

```bash
# Node PATH
export PATH="$PATH:/Users/$USER/node_modules/.bin"
```

## Lint

```bash
npm install markdownlint-cli
npm install remark-cli remark-preset-lint-recommended
npm install prettier
npm install @commitlint/cli @commitlint/config-conventional
echo "module.exports = {extends: ['@commitlint/config-conventional']}" > ~/commitlint.config.js
```

## Misc

```bash
brew cask install macdown vscodium

brew install tree xz yamllint wget

brew install pwgen kafkacat jq gnutls

brew install tiger-vnc

brew install gimp inkscape

```

# Ext4

Create a file called `ext4fuse.rb` and add this code:

```ruby
class MacFuseRequirement < Requirement
  fatal true

  satisfy(build_env: false) { self.class.binary_mac_fuse_installed? }

  def self.binary_mac_fuse_installed?
    File.exist?("/usr/local/include/fuse/fuse.h") &&
      !File.symlink?("/usr/local/include/fuse")
  end

  env do
    ENV.append_path "PKG_CONFIG_PATH", HOMEBREW_LIBRARY/"Homebrew/os/mac/pkgconfig/fuse"

    unless HOMEBREW_PREFIX.to_s == "/usr/local"
      ENV.append_path "HOMEBREW_LIBRARY_PATHS", "/usr/local/lib"
      ENV.append_path "HOMEBREW_INCLUDE_PATHS", "/usr/local/include/fuse"
    end
  end

  def message
    "macFUSE is required. Please run `brew install --cask macfuse` first."
  end
end

class Ext4fuse < Formula
  desc "Read-only implementation of ext4 for FUSE"
  homepage "https://github.com/gerard/ext4fuse"
  url "https://github.com/gerard/ext4fuse/archive/v0.1.3.tar.gz"
  sha256 "550f1e152c4de7d4ea517ee1c708f57bfebb0856281c508511419db45aa3ca9f"
  license "GPL-2.0"
  head "https://github.com/gerard/ext4fuse.git"

  bottle do
    sha256 cellar: :any, catalina:    "446dde5e84b058966ead0cde5e38e9411f465732527f6decfa1c0dcdbd4abbef"
    sha256 cellar: :any, mojave:      "88c4918bf5218f99295e539fe4499152edb3b60b6659e44ddd68b22359f512ae"
    sha256 cellar: :any, high_sierra: "fc69c8993afd0ffc16a73c9c036ca8f83c77ac2a19b3237f76f9ccee8b30bbc9"
    sha256 cellar: :any, sierra:      "fe8bbe7cd5362f00ff06ef750926bf349d60563c20b0ecf212778631c8912ba2"
    sha256 cellar: :any, el_capitan:  "291047c821b7b205d85be853fb005510c6ab01bd4c2a2193c192299b6f049d35"
    sha256 cellar: :any, yosemite:    "b11f564b7e7c08af0b0a3e9854973d39809bf2d8a56014f4882772b2f7307ac1"
  end

  depends_on "pkg-config" => :build

  on_macos do
    depends_on MacFuseRequirement => :build
  end

  on_linux do
    depends_on "libfuse"
  end

  def install
    system "make"
    bin.install "ext4fuse"
  end
end
```

```bash
brew install --cask macfuse
brew install --formula --build-from-source ./ext4fuse.rb
```

```bash
mkdir ~/tmp
```

After installing the Ext4 support software, you now need to determine the hard
drive you want to mount. To do this, run the following command:

```bash
diskutil list
```

Save the partition ID (will look like /dev/disk3s1). Then, run the following
command to mount the hard drive:

```bash
sudo ext4fuse /dev/disk3s1 ~/tmp/ext4_support_PARTITION -o allow_other
```

ext4_support above can be any name you choose. Now, navigate to the `tmp`
directory in the Finder and you will see the contents of the partition listed.
If your drive has multiple partitions, you can mount them using the same steps
as above. Just make sure to use different directory names to mount them.
