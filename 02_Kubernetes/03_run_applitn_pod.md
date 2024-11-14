
<br>
<br>

# `# Run pod in a workerNode: `

<br>
<br>

`POD এর মধ্যে আমাদের container চলবে । POD  হচ্ছে একটা running instance incluster.`
`Pod এ আমরা এক বা একাধিক container রান করতে পারি এবং container গুলো নিজেদের মধ্যে resources শেয়ার করতে পারে । আচ্ছা চলো docker hub থেকে একটা image  । `


[Docker_Hub_Image_Nginx](https://hub.docker.com/_/nginx)

<br>

---
---
---

<br>


# `# 1.1 Pod এর মধ্যে container চলবে । তাই, আগে POD বানাবো । `



### `--- Step: 01 ---`
```bash
kubectl create deployment my-nginx --image=nginx:latest
```
here,
i) my-nginx আমার দেওয়া নাম । 
ii) Docker repo তে image এর নাম nginx দেওয়া আছে । 
iii) nginx:latest হচ্ছে, version নাম । 




### `--- Step: 02 ---`
**For checking,**

```bash
kubectl get deployments
```
**Output:**
```css
NAME       READY   UP-TO-DATE   AVAILABLE   AGE
my-nginx   1/1     1            1           5m56s
```
**here,** 
i) 1/1 means OKay.



### `--- Step: 03 ---`
**For cheking pod:**

```bash
 kubectl get pods 
```

**output:**
```css
NAME                       READY   STATUS    RESTARTS   AGE
my-nginx-c78685b99-4knfl   1/1     Running   0          10m
```
**here,**
i) my-nginx-c78685b99-4knfl pod name
ii) 1/1 everything is okay.

<br>

---
---
---

<br>

# `# 1.2 See the dashboard of minikube: `

```bash
minikube dashboard
```
**output:**
It will give us a link and by following this link we will go to a websites.
From that we will find all the staus about kubernetes.

<br>
<br>
<br>
<br>

---
---
---

<br>
<br>
<br>

# `#2. How to delete container from a pod?  `


Kubernetes-এ **একটি চলমান Pod থেকে সরাসরি কন্টেইনার মুছে ফেলা যায় না**। Pod হলো Kubernetes-এর সবচেয়ে ছোট ইউনিট, যা এক বা একাধিক কন্টেইনার নিয়ে কাজ করে। যদি আপনি কন্টেইনার পরিবর্তন করতে চান, সাধারণত আপনাকে পুরো Pod মুছে ফেলে নতুনভাবে তৈরি করতে হবে।

তবে আপনার উদ্দেশ্য অনুসারে নিচে কিছু উপায় দেওয়া হলো:

### `অপশন 2.1 : পুরো Pod মুছে ফেলা:`
যদি আপনি পুরো Pod (সব কন্টেইনার সহ) মুছে ফেলতে চান, তাহলে নিচের কমান্ড ব্যবহার করুন:

```bash
kubectl delete pod <pod-name>
```

আপনার উদাহরণে, এটি হবে:

```bash
kubectl delete pod my-nginx-c78685b99-4knfl
```

এটি Pod-কে terminate করবে। যদি এটি একটি Deployment-এর অংশ হয় (যেমন `my-nginx`), তাহলে Kubernetes নতুন Pod তৈরি করবে।

### `অপশন 2.2 : Deployment স্কেল ডাউন করা:`
যদি আপনি Deployment ব্যবহার করেন এবং চলমান কন্টেইনারের সংখ্যা কমাতে চান, তাহলে স্কেল ডাউন করতে পারেন:

```bash
kubectl scale deployment my-nginx --replicas=0
```

এটি সব Pod বন্ধ করে দেবে।

আবার চালু করতে চাইলে:

```bash
kubectl scale deployment my-nginx --replicas=1
```

### `অপশন 2.3: Deployment কনফিগারেশন পরিবর্তন করা:`
যদি আপনি একটি multi-container Pod থেকে কোনো কন্টেইনার সরাতে চান, তাহলে Deployment-এর কনফিগারেশন আপডেট করতে হবে।

1. Deployment সম্পাদনা করতে:

   ```bash
   kubectl edit deployment my-nginx
   ```

2. YAML ফাইলের `containers` সেকশন থেকে অপ্রয়োজনীয় কন্টেইনারটি মুছে ফেলুন।
3. পরিবর্তন সেভ করে বের হয়ে আসুন।

Kubernetes পরিবর্তনগুলো প্রয়োগ করবে এবং নতুন Pod তৈরি করবে।

### `অপশন 2.4: Pod মুছে ফেলে নতুন কনফিগারেশন প্রয়োগ করা:`
যদি আপনার কাছে শুধুমাত্র Pod থাকে (Deployment নয়), তাহলে Pod মুছে ফেলে নতুনভাবে তৈরি করুন।

1. Pod মুছে ফেলুন:

   ```bash
   kubectl delete pod my-nginx-c78685b99-4knfl
   ```

2. YAML ফাইল বা `kubectl run` কমান্ড ব্যবহার করে নতুন Pod তৈরি করুন।



