
---

<br>
<br>

# `Kubernetes`

<br>
<br>

---

# `#1. First,install kubectl `
[from_official_websites](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)


After successfully installing `kubclt` run the command and the output will be like below:
    ```bash
    kubectl version --client              
    Client Version: v1.31.2
    Kustomize Version: v5.4.2
    ```

From the end of the website. then install: Minikub

# `#2. Install Minikube: `

### `#2.1`

After successfully installing `minikube` run the command and the output will be like below:

```bash
 minikube status
```

```css
🤷  Profile "minikube" not found. Run "minikube profile list" to view all profiles.
👉  To start a cluster, run: "minikube start"
```
<br>

### `#2.2`

Then run: 

```bash
 minikube start
```
<br>

we get an error:

```css
Exiting due to DRV_DOCKER_NOT_RUNNING: Found docker, but the docker service isn't running. Try restarting the docker service.
```

The error message indicates that Minikube is trying to use Docker as the default driver but cannot connect because the Docker daemon is not running. Here’s how you can fix it.

### Solution 1: Start the docker deamon:

1. **Check Docker Status:**

   ```bash
   systemctl status docker
   ```

2. **Start Docker Service:**
   If it’s not running, start the Docker service:

   ```bash
   sudo systemctl start docker
   ```

3. **Enable Docker to Start on Boot:**
   ```bash
   sudo systemctl enable docker
   ```

4. **Verify Docker is Running:**
   ```bash
   docker info
   ```

5. **After that make a group run the below command:** 

    ```bash
    sudo usermod -aG docker $USER
    ```

6. **After running this command, apply the changes with:**

    ```bash
    newgrp docker
    ```

7. **Try again:**
    ```bash
    minikube start --driver=docker
    ```

<br>
<br>
<br>


`After doing all of these step if we get error then first install minikube ctl. and from minikube install the required version of kubectl. `

T
1. **Remove the Incorrect Binary Again (Just in Case)**
   Run this to ensure it's deleted:

   ```bash
   sudo rm -f /usr/local/bin/kubectl
   ```

2. **Reinstall `kubectl` Using the Package Manager**
   Use Arch Linux's package manager (`pacman`) to install the correct version:

   ```bash
   sudo pacman -S kubectl
   ```

3. **Verify the New Installation**
   Confirm the correct architecture:

   ```bash
   which kubectl
   file $(which kubectl)
   ```

   The output should indicate `ELF 64-bit LSB executable, x86-64`.

4. **Check the Minikube `kubectl` Version**
   Sometimes Minikube has its own bundled version of `kubectl`. Ensure it uses the correct one:

   ```bash
   minikube kubectl version
   ```

5. **Force Minikube to Use the System `kubectl`**
   Set the environment variable to override:

   ```bash
   export MINIKUBE_KUBECTL=/usr/bin/kubectl
   ```

   Or you can configure it permanently in your shell configuration file (`~/.zshrc` or `~/.bashrc`):

   ```bash
   echo 'export MINIKUBE_KUBECTL=/usr/bin/kubectl' >> ~/.zshrc
   source ~/.zshrc
   ```

6. **Restart Minikube**
   Finally, restart Minikube:

   ```bash
   minikube stop
   minikube start
   ```

If the problem persists, please let me know the output of:

```bash
echo $PATH
minikube kubectl version
```


যদি কোন ঝামেলা হয় । তাহলে, আবার, dokcer user  "sudo usermod -aG docker $USER" করবো । তারপর আগের মতো বাকী স্টেপ গুলো ফলো করবো । 



