# Argo MicroK8s

```
sudo usermod -aG wheel,docker bsmith

sudo iptables -P FORWARD ACCEPT

sudo iptables-save > /etc/sysconfig/iptables

sudo systemctl disable firewalld

sudo systemctl stop firewalld

sudo vi /etc/selinux/config

sudo ln -sf /var/lib/snapd/snap /snap

sudo snap install microk8s --classic
```

## Config

```
microk8s.kubectl config view --raw > $HOME/.kube/config

sudo snap alias microk8s.kubectl kubectl

microk8s.enable dns

microk8s.enable ingress

microk8s.enable dashboard

kubectl patch svc kubernetes-dashboard -n kube-system -p '{"spec": {"type": "LoadBalancer"}}'

microk8s.enable storage

microk8s.enable ingress

microk8s.enable registry

microk8s.enable prometheus
```

## ArgoCD

```
curl -sSL -o ~/bin/argocd https://github.com/argoproj/argo-cd/releases/download/v1.0.0/argocd-linux-amd64

chmod +x ~/bin/argocd

kubectl create namespace argocd

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
```

```
argocd login 192.168.1.203:30209

argocd app create guestbook   --repo https://github.com/argoproj/argocd-example-apps.git   --path guestbook   --dest-server https://kubernetes.default.svc   --dest-namespace default
```

## Argo Workflow

```
curl -sSL -o ~/bin/argo https://github.com/argoproj/argo/releases/download/v2.2.1/argo-linux-amd64

chmod +x ~/bin/argo

kubectl create ns argo

kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/v2.2.1/manifests/install.yaml

kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=default:default

argo list

kubectl patch svc argo-ui -n argo -p '{"spec": {"type": "LoadBalancer"}}'

argo submit --watch https://raw.githubusercontent.com/argoproj/argo/master/examples/hello-world.yaml

argo submit --watch https://raw.githubusercontent.com/argoproj/argo/master/examples/coinflip.yaml

argo submit --watch https://raw.githubusercontent.com/argoproj/argo/master/examples/loops-maps.yaml
```
