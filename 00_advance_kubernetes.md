<br>
<br>
<br>


# `#1.1 Kubernetes Cluster SetUP: `

Kubernetes ক্লাস্টার সেটআপ করার জন্য বিভিন্ন ধরণের টুলস এবং প্ল্যাটফর্ম রয়েছে। আমরা কোন পরিবেশে (on-premise, ক্লাউড, বা হাইব্রিড) সেটআপ করবেন তার উপর নির্ভর করে টুলস আলাদা হতে পারে। নিচে তালিকা দেয়া হলো:

---

### **1. Cloud-Based Kubernetes Tools**
ক্লাউড প্রোভাইডাররা Kubernetes ক্লাস্টার সেটআপের জন্য ম্যানেজড সার্ভিস দেয়। এগুলি সহজে ব্যবস্থাপনা এবং স্কেলিংয়ের জন্য আদর্শ।

- **Google Kubernetes Engine (GKE)**  
  Google Cloud-এ Kubernetes ক্লাস্টার তৈরি ও ব্যবস্থাপনা সহজ করে।
  
- **Amazon Elastic Kubernetes Service (EKS)**  
  AWS-এ ম্যানেজড Kubernetes ক্লাস্টার তৈরি ও পরিচালনার জন্য।
  
- **Azure Kubernetes Service (AKS)**  
  Microsoft Azure-এ Kubernetes ক্লাস্টার ডেপ্লয় ও পরিচালনার জন্য।
  
- **IBM Kubernetes Service**  
  IBM Cloud-এ Kubernetes ক্লাস্টার সেটআপের জন্য।
  
- **Oracle Container Engine for Kubernetes (OKE)**  
  Oracle Cloud-এ Kubernetes ক্লাস্টার ডেপ্লয় করার জন্য।


---

### **2. On-Premise বা Bare Metal Tools**
যদি ক্লাউড ব্যবহার না করেন এবং নিজের সার্ভারে Kubernetes ক্লাস্টার তৈরি করতে চান, তাহলে এই টুলগুলো ব্যবহার করতে পারেন।

- **Kubeadm**  
  অফিসিয়াল Kubernetes ক্লাস্টার সেটআপ টুল। কাস্টমাইজেশনের জন্য উপযুক্ত।

- **Rancher**  
  Kubernetes ক্লাস্টার ম্যানেজমেন্ট টুল যা সহজেই ক্লাস্টার সেটআপ ও মেইনটেইন করতে সাহায্য করে।

- **MicroK8s**  
  Canonical দ্বারা ডেভেলপড। Lightweight এবং ছোট স্কেলে Kubernetes ক্লাস্টার তৈরি করার জন্য।

- **K3s**  
  Rancher-এর লাইটওয়েট Kubernetes ডিস্ট্রিবিউশন। IoT এবং edge ডিপ্লয়মেন্টের জন্য আদর্শ।

- **Minikube**  
  লোকাল Kubernetes ক্লাস্টার তৈরি করতে ব্যবহৃত হয়। প্রধানত ডেভেলপমেন্ট ও টেস্টিংয়ের জন্য।

- **OpenShift**  
  Red Hat-এর Kubernetes ডিস্ট্রিবিউশন। এটিতে বিল্ট-ইন CI/CD এবং DevOps টুল রয়েছে।

---

### **3. Hybrid Kubernetes Tools**
যদি আপনি on-premise(লোকাল পিসি) এবং ক্লাউড উভয়ের সমন্বয়ে কাজ করতে চান, তাহলে এই টুলগুলি সহায়ক:

- **Anthos (Google Cloud)**  
  ক্লাউড এবং অন-প্রিমাইজ উভয়েই Kubernetes ক্লাস্টার ম্যানেজ করতে সাহায্য করে।

- **VMware Tanzu**  
  Multi-cloud এবং on-premise Kubernetes ক্লাস্টার ম্যানেজমেন্টের জন্য।

- **Azure Arc**  
  Azure-এর মাধ্যমে on-premise এবং multi-cloud Kubernetes ক্লাস্টার ম্যানেজ করার জন্য।

- **Red Hat OpenShift**  
  Multi-cloud ও on-premise ব্যবহারের জন্য একটি পূর্ণাঙ্গ প্ল্যাটফর্ম।

---

### **4. Cluster Management Tools**
ক্লাস্টার তৈরি ও ম্যানেজ করার জন্য ব্যবহৃত হয়:

- **Helm**  
  Kubernetes-এ অ্যাপ্লিকেশন ডিপ্লয় ও ম্যানেজ করার জন্য।

- **Kubectl**  
  Kubernetes ক্লাস্টারের জন্য কমান্ড-লাইন ইন্টারফেস।

- **Terraform**  
  Kubernetes ক্লাস্টার ইনফ্রাস্ট্রাকচার তৈরি ও পরিচালনার জন্য।

- **Ansible**  
  Kubernetes ক্লাস্টারের জন্য অটোমেশন টুল।

- **K9s**  
  Kubernetes ক্লাস্টার ম্যানেজ করার একটি টার্মিনাল UI টুল।

---


<br>
<br>
<br>

# `#1.2 Kubernetes Pod Creation: `

<br>
<br>
<br>


কুবেরনেটসে পড তৈরি করার দুটি পদ্ধতি রয়েছে: **ডিক্লারেটিভ (Declarative)** এবং **ইম্পারেটিভ (Imperative)**। 


### `**Declarative Way:**`
ডিক্লারেটিভ পদ্ধতিতে আপনি পডের অবস্থা বা কনফিগারেশন একটি YAML বা JSON ফাইলের মাধ্যমে নির্ধারণ করেন। কুবেরনেটস সেই ফাইলটি দেখে পডটি তৈরি বা ম্যানেজ করে।

#### **ধাপসমূহ**:
1. একটি YAML ফাইল তৈরি করুন, যেখানে পডের কনফিগারেশন থাকবে (`pod.yaml` নামের ফাইল)।
2. `kubectl apply` কমান্ড দিয়ে YAML ফাইলটি প্রয়োগ করুন।

#### **উদাহরণ**:
`pod.yaml` ফাইল:

```yaml
apiVersion: v1 (pod এর version normally v1 হয়। )
kind: Pod   (আমরা কি বানাচ্ছি Pod)
metadata: (Pod সম্পকিত তথ্য)
  name: my-pod 
spec:  (container সম্পকিত তথ্য, এক বা একাধিক container থাকতে পারে । )
  containers:
  - name: my-container
    image: nginx
```

ফাইল প্রয়োগ করার কমান্ড:
```bash
kubectl apply -f pod.yaml
```

#### **ডিক্লারেটিভ পদ্ধতির বৈশিষ্ট্য**:
- এই পদ্ধতিতে পড বা অবজেক্টের কাঙ্ক্ষিত অবস্থা সংজ্ঞায়িত করা হয়।
- এটি ইনফ্রাস্ট্রাকচার অ্যাজ কোড (IaC) পদ্ধতির সাথে সামঞ্জস্যপূর্ণ।
- আপনি সহজেই পড কনফিগারেশন আপডেট করতে এবং ট্র্যাক করতে পারেন।

---

## `**Imperative way:**`
ইম্পারেটিভ পদ্ধতিতে সরাসরি কমান্ডের মাধ্যমে পড তৈরি করা হয়। এই পদ্ধতিতে YAML ফাইল তৈরি করার প্রয়োজন হয় না। 


<br>
<br>
<br>

# `#1.3 ReplicaSet in Kubernetes: `

<br>
<br>
<br>

### ReplicaSet in Kubernetes:

Kubernetes-এ **ReplicaSet** একটি অবজেক্ট যা  অ্যাপ্লিকেশনের পডগুলোর নির্দিষ্ট সংখ্যক কপি করতে ব্যবহৃত হয়। সহজভাবে বলতে গেলে, ReplicaSet Kubernetes-এ একটি সার্ভিস যা পডের নির্দিষ্ট সংখ্যা সবসময় চালু রাখে, যাতে কোনো কারণে পড ডাউন হলে অন্য পডগুলি চালু থাকে এবং সার্ভিসটি downtime না দেখা দেয় । 

#### **ReplicaSet কীভাবে কাজ করে?**

ধরা যাক,  একটি ওয়েব সার্ভার চলতেছে যা ৫টি পডে রান করতেছে । যদি একটি পড হঠাৎ করে ক্র্যাশ হয়ে যায় বা কোনো কারণে ডাউন হয়ে যায়, তাহলে ReplicaSet স্বয়ংক্রিয়ভাবে নতুন একটি পড তৈরি করবে, যাতে মোট পডের সংখ্যা ৫টি থাকে। এটি **high availability** নিশ্চিত করে।

#### **ReplicaSet এর উদ্দেশ্য:**

1. **পডের সংখ্যা নির্ধারণ করা**: ReplicaSet নিশ্চিত করে যে কোনো সময়ে নির্দিষ্ট সংখ্যক পড চালু থাকবে।
   
2. **অটোমেটিক রিকভারি**: যদি কোনো পড কাজ না করে, ReplicaSet সেটি পুনরায় চালু করে। এটি একটি প্রক্রিয়া যেখানে পডের গতি এবং স্বাস্থ্য মনিটর করা হয় এবং কোনো সমস্যা দেখা দিলে সেই পড পুনরায় তৈরি করা হয়।

3. **স্কেলিং**: ReplicaSet ব্যবহার করে পডের সংখ্যা সহজেই বাড়ানো বা কমানো যেতে পারে।

#### **ReplicaSet এর কনফিগারেশন:**

ReplicaSet একটি `spec` ফিল্ডে পডের ডিফিনিশন এবং পডের সংখ্যা কনফিগার করে। উদাহরণস্বরূপ:

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-replicaset
spec:
  replicas: 3  # এখানে ৩টি পড চালু থাকবে
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app-container
        image: my-app-image:latest
```

#### **ReplicaSet এর উপাদানগুলো:**

- **replicas**: এখানে আমরা নির্দিষ্ট করে দেই যে আমাদের কতগুলো পড থাকবে। উদাহরণস্বরূপ, ৩টি পড।
  
- **selector**: এটি ব্যবহার করে ReplicaSet জানে কোন পডগুলো সে পরিচালনা করবে। সাধারণত, এটি পডের লেবেল ব্যবহার করে।
  
- **template**: এই অংশে আমরা পডের কাঠামো বা কনফিগারেশন নির্দিষ্ট করি, যেমনঃ কোন কনটেইনার ইমেজ ব্যবহার হবে, পোর্ট কি হবে, ইত্যাদি।

#### **ReplicaSet এবং Deployment এর মধ্যে পার্থক্য:**

- **ReplicaSet** শুধুমাত্র পডের কপি চালু রাখতে ব্যবহার করা হয়।
- **Deployment** একটি উচ্চতর অবজেক্ট যা ReplicaSet তৈরি করে এবং পডের আপগ্রেড বা রোলব্যাকের মতো কাজগুলোও পরিচালনা করে।

এভাবে, **ReplicaSet** Kubernetes-এ নিশ্চিত করে যে আপনার অ্যাপ্লিকেশন নির্দিষ্ট সংখ্যক কপি চালু থাকবে, এবং কোনো পড ডাউন হলে সেটি স্বয়ংক্রিয়ভাবে পুনরায় তৈরি করা হবে।



<br>
<br>
<br>


#  `#1.4 Disadvanage of ReplicaSet and introduction to Deployment : `

<br>
<br>
<br>


## **ReplicaSet-এর অসুবিধাগুলো**  
ReplicaSet মূলত Kubernetes-এ পড (Pod) সংখ্যা নির্ধারণ করে, কিন্তু কিছু সীমাবদ্ধতাও রয়েছে:

#### ১. **পুরনো Version ম্যানেজমেন্ট নেই**  
- ReplicaSet শুধুমাত্র একটি নির্দিষ্ট Version পড চালাতে পারে।  
- যদি কোনো নতুন version আপডেট বা রোল আউট করবো, পুরনো সকল Pod বা ReplicaSet গুলো  মুছে  যায় ফলে আমরা application এ downtime দেখা যায় ।  

#### ২. **রোলিং আপডেট সাপোর্ট নেই**  
- ReplicaSet নতুন কোড রোল আউট করার জন্য পর্যায়ক্রমে পুরনো পডগুলো পরিবর্তন করতে পারে না।  
- এটি একবারে সব পড বন্ধ করে নতুন পড চালায়, ফলে অ্যাপ্লিকেশন ডাউনটাইম হয় ।   



## **Deployment: Docker-এর পরিচিতি**
Deployment হলো **Docker** বা Kubernetes-এ একটি অ্যাপ্লিকেশন চালু করার প্রক্রিয়া, যেখানে কোড, কনফিগারেশন, এবং ডিপ্লয়মেন্ট স্ট্র্যাটেজি একত্রে থাকে। 



### **Docker Deployment কীভাবে কাজ করে?**
Docker Deployment অ্যাপ্লিকেশন কনটেইনারাইজ করে। এর মাধ্যমে অ্যাপ্লিকেশন সহজে চালানো, স্কেল করা এবং পরিচালনা করা যায়।

#### Docker Deployment-এর প্রধান ধাপ:
১. **Dockerfile তৈরি করা:**  
   অ্যাপ্লিকেশন কীভাবে চলবে, তা সংজ্ঞায়িত করতে একটি `Dockerfile` তৈরি করা হয়।  

২. **Docker Image তৈরি করা:**  
   `Dockerfile` থেকে অ্যাপ্লিকেশনের জন্য একটি Docker Image বানানো হয়।  

৩. **কনটেইনার চালানো:**  
   তৈরি করা ইমেজ থেকে কনটেইনার চালানো হয়।  

Deployment এ পুরনো সকল Pod বা ReplicaSet গুলো  মুছে  যায় না, code update করলে, একটা একটা করে pod এ নতুন কোড বা version update হয়, এর ফলে আমরা application এ downtime দেখা যায় না। 

<br>
<br>
<br>


#  `#1.4 Combine ReplicaSet In Deploymnet File: `

<br>
<br>
<br>

যখন আমরা একটি **Deployment** তৈরি করবো, এটি স্বয়ংক্রিয়ভাবে একটি **ReplicaSet** তৈরি করে। **Deployment** নিশ্চিত করে যে নির্দিষ্ট সংখ্যক পড একই সময়ে চালু থাকবে। আর **ReplicaSet** হল সেই অবজেক্ট যা পডের নির্দিষ্ট সংখ্যা চালু রাখে এবং যদি কোনো পড ক্র্যাশ হয়ে যায়, তবে সেটি পুনরায় তৈরি করে।

### উদাহরণ: **Deployment** YAML ফাইলে **ReplicaSet** ব্যবস্থাপনাঃ 

এখানে একটি **Deployment** YAML ফাইলের উদাহরণ দেওয়া হল, যা পেছনে একটি **ReplicaSet** পরিচালনা করে:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-fastapi-deployment
spec:
  replicas: 3  # পডের সংখ্যা
  selector:
    matchLabels:
      app: my-fastapi-app
  template:
    metadata:
      labels:
        app: my-fastapi-app
    spec:
      containers:
        - name: fastapi-container
          image: yasin005/fastapi_db:01  # আপনার ইমেজের নাম
          ports:
            - containerPort: 80
```

### YAML ফাইলের ব্যাখ্যা:
- **apiVersion: apps/v1**: কুবেরনেটিসে ডিপ্লয়মেন্ট পরিচালনার জন্য API ভার্সন।
- **kind: Deployment**: এখানে আমরা **Deployment** অবজেক্ট ব্যবহার করছি।
- **metadata**: ডিপ্লয়মেন্টের নাম এবং অন্যান্য তথ্য।
- **spec**:
  - **replicas**: পডের সংখ্যা (এখানে ৩টি)। কুবেরনেটিস নিশ্চিত করবে যে ৩টি পড সবসময় চলমান থাকবে।
  - **selector**: ডিপ্লয়মেন্টের পডগুলোকে সনাক্ত করার জন্য লেবেল ব্যবহার করে (এখানে `app: my-fastapi-app` লেবেল দিয়ে পড সিলেক্ট করা হচ্ছে)।
  - **template**: পডের টেমপ্লেট যা ডিপ্লয়মেন্ট তৈরি করবে।
    - **metadata**: পডের লেবেল।
    - **spec**: পডের কনটেইনার এবং অন্যান্য কনফিগারেশন যেমন ইমেজ এবং পোর্ট।

### **ReplicaSet** এর সাথে কিভাবে এটি যুক্ত হয়?
- যখন আপনি একটি **Deployment** তৈরি করেন, কুবেরনেটিস পেছনে একটি **ReplicaSet** স্বয়ংক্রিয়ভাবে তৈরি এবং পরিচালনা করে, যেটি পডের সংখ্যা নিশ্চিত করে।
- **ReplicaSet** নিশ্চিত করে যে নির্দিষ্ট সংখ্যক পড চলমান থাকবে। যদি কোনো পড ডাউন হয়ে যায়, ReplicaSet সেটি পুনরায় তৈরি করে।
- **Deployment** সহজেই অ্যাপ্লিকেশন আপডেট, স্কেল এবং রোলব্যাক করার জন্য ব্যবহৃত হয়, আর **ReplicaSet** কেবল পডের সংখ্যা পরিচালনা করে।

### **ReplicaSet** এবং **Deployment** এর মধ্যে পার্থক্য:
- **ReplicaSet** কেবল পডের কপি চালু রাখার কাজ করে।
- **Deployment** একটি উচ্চতর অবজেক্ট যা **ReplicaSet** তৈরি করে এবং পডের আপডেট, রোলব্যাকের মতো কাজগুলো পরিচালনা করে।

### কেন **Deployment** ব্যবহার করবেন এবং **ReplicaSet** না?
- **Deployment** একটি উচ্চ স্তরের অ্যাবস্ট্রাকশন। আপনাকে **ReplicaSet** ম্যানুয়ালি পরিচালনা করতে হয় না। 
- **Deployment** আপনার অ্যাপ্লিকেশন আপডেট এবং রোলব্যাক করতেও সহায়ক।
- **Deployment** ব্যবহারের মাধ্যমে আপনি **zero-downtime** আপডেট পেতে পারেন, অর্থাৎ, নতুন ভার্সনে আপডেট করা হলেও অ্যাপ্লিকেশন ব্যবহারে কোনো বিঘ্ন ঘটবে না।

### উপসংহার:
কুবেরনেটিসের **Deployment** YAML ফাইলে একটি **ReplicaSet** স্বয়ংক্রিয়ভাবে ব্যবস্থাপিত হয় এবং আপনাকে এটি আলাদাভাবে সংজ্ঞায়িত করার প্রয়োজন হয় না। আপনি কেবলমাত্র আপনার প্রয়োজনীয় স্টেট (পডের সংখ্যা, পডের কনফিগারেশন, ইত্যাদি) **Deployment** এ সংজ্ঞায়িত করেন এবং কুবেরনেটিস বাকি কাজটি স্বয়ংক্রিয়ভাবে করে দেয়।


<br>
<br>
<br>


#  `#1.5 NameSpace in kubernetes: `

<br>
<br>
<br>


ধরি, এখানে **তিনজন ইউজার** আছে:  
1. **1ম ইউজার:** ৩টা পড বানালো।  
2. **2য় ইউজার:** আরও ৩টা পড বানালো।  
3. **3য় ইউজার:** ১ম ইউজারের পড চেঞ্জ করে দিলো, আর ২য় ইউজারের পড ডিলিট করলো।  

এখন শুরুতে, আমরা যখন পড বানায় তখন সেইটা ডিফল্ট জায়গায় (default Namespace) তৈরি হয় । কিন্তু, এখানে সমস্যা হচ্ছে:  
- ৩য় ইউজার সহজেই অন্য ইউজারদের পডে পরিবর্তন আনতে বা মুছে ফেলতে পারে।  
- কোনো আলাদা নিয়ন্ত্রণ (permission) নেই।  

---

### **Namespace হলো এই সমস্যার সমাধানঃ **  
Namespace দিয়ে আমরা প্রতিটি ইউজারের জন্য আলাদা space তৈরি করতে পারি। এতে এক ইউজার অন্য ইউজারের পডে হাত দিতে পারবে না। 

---

### **Namespace উদাহরণে কাজের ধাপ:**  

#### **১. আলাদা Namespace বানাই:**  
প্রতিটি ইউজারের জন্য আলাদা Namespace তৈরি করি:  
```bash
kubectl create namespace user1-space
kubectl create namespace user2-space
kubectl create namespace user3-space
```

#### **২. পড বানানো আলাদা Namespace-এ:**  
**1ম ইউজার** তার পডগুলো `user1-space` Namespace-এ রাখবে:  
**2য় ইউজার** তার পডগুলো `user2-space` Namespace-এ রাখবে।  
**3য় ইউজার** তার পডগুলো `user3-space` Namespace-এ রাখবে।  

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: amar-app
  namespace: amar-khelar-math # এখানে Namespace উল্লেখ করো
spec:
  replicas: 2
  selector:
    matchLabels:
      app: amar-app
  template:
    metadata:
      labels:
        app: amar-app
    spec:
      containers:
      - name: amar-container
        image: nginx
        ports:
        - containerPort: 80

```


#### **৩. Namespace-ভিত্তিক নিয়ন্ত্রণ (RBAC):**  
**RBAC (Role-Based Access Control)** ব্যবহার করে প্রতিটি ইউজারকে শুধু তার Namespace ব্যবহারের অনুমতি দেওয়া হয়।  
- **1ম ইউজার** শুধু `user1-space` Namespace-এ কাজ করতে পারবে।  
- **2য় ইউজার** শুধু `user2-space` Namespace-এ কাজ করতে পারবে।  
- **3য় ইউজার** অন্য কারো Namespace-এ কিছু করতে পারবে না।  

---

### **Namespace-এ কাজ করার কমান্ড:**  

1. **Namespace-এ পড তৈরি করা:**  
   ```bash
   kubectl apply -f user1-pod.yaml
   ```

2. **Namespace-এ পড লিস্ট দেখা:**  
   ```bash
   kubectl get pods -n user1-space
   ```

3. **একটি নির্দিষ্ট Namespace-এর পড ডিলিট করার চেষ্টা:**  
   যদি ৩য় ইউজার `user1-space`-এ কিছু করতে চায়, RBAC তাকে বাধা দেবে।  

4. **see all the namespace:**
  ```bash
  kubectl get namespaces
  ```

---
---
---

## `**Kubernetes-এর Default Namespaces:**`

Kubernetes-এ কিছু **ডিফল্ট Namespace** থাকে, যেগুলো ক্লাস্টার তৈরি হলে নিজে থেকেই সেটআপ হয়ে যায়। প্রতিটি Namespace-এর আলাদা কাজ ও উদ্দেশ্য থাকে। নিচে এগুলো নিয়ে বিস্তারিত ব্যাখ্যা করা হলো:

---

### **1. `default` Namespace**
- **উদ্দেশ্য:**  
  এটা Kubernetes-এর প্রধান Namespace।  
  যখন কোনো অ্যাপ্লিকেশন বা রিসোর্স তৈরি করা হয় এবং Namespace উল্লেখ করা হয় না, তখন সেটা **`default` Namespace**-এ চলে যায়।

- **ব্যবহার:**  
  সাধারণ ব্যবহারকারীদের জন্য, যারা আলাদা Namespace তৈরি করতে চায় না।  
  ছোট প্রজেক্ট বা টেস্টিংয়ের জন্য উপযুক্ত।  

- **উদাহরণ:**  
  নিচের পড তৈরি করলে এটা `default` Namespace-এ যাবে:  
  ```bash
  kubectl create pod my-pod --image=nginx
  ```
  বা,  
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: my-pod
  spec:
    containers:
    - name: nginx
      image: nginx
  ```

---

### **2. `kube-system` Namespace**
- **উদ্দেশ্য:**  
  এটি Kubernetes ক্লাস্টারের নিজস্ব সিস্টেম কম্পোনেন্ট (যেমন, API server, Controller Manager, Scheduler) এর জন্য সংরক্ষিত।  
  এখানে ক্লাস্টারের মেইনটেনেন্স সম্পর্কিত কাজ হয়।  

- **ব্যবহার:**  
  **Cluster Admins** এই Namespace ব্যবহার করে ক্লাস্টারের সিস্টেম লজিক দেখতে বা ডিবাগ করতে।  
  ব্যবহারকারীরা সাধারণত এখানে কিছু পরিবর্তন করে না।  

- **উদাহরণ:**  
  `kube-system` Namespace-এ চলমান পডগুলো দেখতে:  
  ```bash
  kubectl get pods -n kube-system
  ```
  এখানে তুমি **CoreDNS, kube-proxy** এর মতো সিস্টেম পড দেখতে পাবে।

---

### **3. `kube-public` Namespace**
- **উদ্দেশ্য:**  
  এই Namespace সবার জন্য উন্মুক্ত।  
  সাধারণত এমন ডেটা বা রিসোর্স রাখার জন্য ব্যবহার করা হয় যা ক্লাস্টারের ভেতরের বা বাইরের সবাই দেখতে পারে।  

- **ব্যবহার:**  
  এটা খুব কম ব্যবহার করা হয়।  
  কিছু পাবলিক ডেটা শেয়ার করার জন্য উপযুক্ত, যেমন ক্লাস্টারের কনফিগারেশন।

- **উদাহরণ:**  
  এখানে পাবলিক ডেটা দেখতে:  
  ```bash
  kubectl get all -n kube-public
  ```

---

### **4. `kube-node-lease` Namespace**
- **উদ্দেশ্য:**  
  **Node Leases**-এর জন্য সংরক্ষিত।  
  Kubernetes প্রতিটি নোডের জন্য একটি **Lease Object** তৈরি করে। এই Lease Object নোডের হার্টবিট (লাইভ স্ট্যাটাস) ট্র্যাক করতে সাহায্য করে।  

- **কেন গুরুত্বপূর্ণ?**  
  এটি **Node Health Monitoring** আরও দ্রুত ও কার্যকর করে।  
  যদি একটি নোড ক্লাস্টারের সাথে সংযোগ হারায়, Kubernetes এই Lease Object ব্যবহার করে দ্রুত তা শনাক্ত করতে পারে।  

- **ব্যবহার:**  
  সাধারন ব্যবহারকারীদের এখানে কাজ করার দরকার হয় না।  
  **Cluster Admins** এটা ডিবাগ করার সময় দেখতে পারেন।  

- **উদাহরণ:**  
  `kube-node-lease`-এর সমস্ত রিসোর্স দেখতে:  
  ```bash
  kubectl get leases -n kube-node-lease
  ```

---

### **Namespace-এর গুরুত্ব:**
- প্রতিটি Namespace একটি আলাদা **লজিকাল গ্রুপ** তৈরি করে।  
- এর ফলে একে অপরের কাজ বা রিসোর্সে প্রভাব ফেলতে পারে না।  
- ক্লাস্টার ম্যানেজমেন্ট আরও সুসংগঠিত হয়।  

---

### **উপসংহার:**
Kubernetes-এর **Default Namespaces**:
- **`default`:** সাধারণ অ্যাপ্লিকেশনের জন্য।  
- **`kube-system`:** Kubernetes-এর নিজস্ব সিস্টেম কম্পোনেন্টের জন্য।  
- **`kube-public`:** সবাই দেখতে পারে এমন রিসোর্সের জন্য।  
- **`kube-node-lease`:** নোডের লাইভ স্ট্যাটাস দেখার জন্য ।   


### `**Resource Quota:**`
এখন কথা, হচ্ছে আমরা namespace use করলাম, এখন যদি একটা user অনেকগুলো একটা namespace এর 
মধ্যে অনেক গুলো pod create করে তাহলে, অন্য user এর জন্য hardware resource কমে যাবে । এখন, আমরা Resource Quota দিইয়ে Namespace-এর মধ্যে রিসোর্স ব্যবহারের সীমা নির্ধারণ করে। এটি ক্লাস্টারে প্রতিটি টিম বা অ্যাপ্লিকেশনকে একটি নির্দিষ্ট পরিমাণ রিসোর্স ব্যবহার করার সুযোগ দেয়, যাতে অন্যদের রিসোর্স ব্যবহার প্রভাবিত না হয়।

**application in deployment.yml file:**

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: dev-namespace  # The deployment will be in the dev-namespace
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        resources:
          requests:
            memory: "1Gi"      # Requesting 1Gi memory
            cpu: "500m"        # Requesting 500m CPU (half a core)
          limits:
            memory: "2Gi"      # Limiting memory usage to 2Gi
            cpu: "1"           # Limiting CPU usage to 1 core
```

`Note: recourse limit দেওয়ার আগে, আমাদের আগে ResourceQuota.yml file apply করতে হবে । see, 04_create_namespace `


<br>
<br>
<br>


#  `#1.5 kubernetes Services:  `

<br>
<br>
<br>


এখন আমরাদের একটা pod এর মধ্যে একটা application deploy করেছি। উপরে বর্ণনা করেছি, কীভাবে একটা application একটা pod এর মধ্যে  deploy করা লাগে । এখন, এই application এর একটা ip address আছে। যদি আমরা pod কে delete করে নতুন একটা pod make করি তাহলে ip address change হয়ে যাবে । বা, application টি এক app থেকে অন্য একটা app এ নিয়ে গেলে ip address change হয়ে যাবে । এখন, application টির ip address যদি dynamic nature এর হয় তাহলে আমরা একে access কীভাবে করবো ? এর জন্য kubernetes এ আমরা Services ব্যবহার করি । 



Kubernetes-এ **Service** ব্যবহার করে আমরা একটি Pod বা Pods-কে **স্ট্যাটিক IP address** দিয়ে অ্যাক্সেস করতে পারি। যখনই Pod-এর IP অ্যাড্রেস পরিবর্তিত হয়, **Service** সেই পরিবর্তন ট্র্যাক করে এবং নির্ধারিত **Cluster IP** ব্যবহার করে অ্যাপ্লিকেশন অ্যাক্সেসযোগ্য রাখে। **Service** মূলত একটি স্থায়ী নেটওয়ার্ক ইন্টারফেস তৈরি করে, যা Pods-কে **load balancing** এর মাধ্যমে অ্যাক্সেস দেয়।

### **Service.yml Configuration**

নিচে একটি উদাহরণ দেওয়া হলো, যেখানে একটি **Service** একটি Pod-কে এক্সপোজ করছে:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service          # Service-এর নাম
  labels:
    app: my-app
spec:
  selector:
    app: my-app             # এটি নির্ধারণ করে কোন Pods-এর জন্য Service প্রযোজ্য
  ports:
    - protocol: TCP
      port: 80              # Service-এর মাধ্যমে অ্যাক্সেসযোগ্য পোর্ট
      targetPort: 8080      # Pod-এর ভেতরে চলমান অ্যাপ্লিকেশনের পোর্ট
  type: ClusterIP           # Service টাইপ (Default: ClusterIP)
```

---

### **Configuration Details**
1. **apiVersion**: এটি Kubernetes API-এর ভার্সন। এখানে `v1` ব্যবহার করা হয়েছে।
2. **kind**: এটি Service এর টাইপ নির্ধারণ করে।
3. **metadata**: 
   - **name**: Service এর নাম, যা এটি চিহ্নিত করার জন্য ব্যবহৃত হয়।
   - **labels**: Pods-এর সাথে **Service** কে লিঙ্ক করতে সাহায্য করে।
4. **spec**: Service-এর স্পেসিফিকেশন।
   - **selector**: এটি নির্ধারণ করে যে কোন Pods-এর জন্য Service কাজ করবে। এখানে `app: my-app` লেবেলযুক্ত Pods নির্বাচন করা হয়েছে।
   - **ports**:
     - **protocol**: কোন প্রোটোকল (TCP/UDP) ব্যবহার করা হবে।
     - **port**: Service-এর পোর্ট, যেটা ব্যবহারকারীরা অ্যাক্সেস করবে।
     - **targetPort**: Pod-এর ভেতরে চলমান অ্যাপ্লিকেশনের পোর্ট।
   - **type**: Service টাইপ। Default `ClusterIP`। অন্যান্য টাইপ:
     - **NodePort**: সার্ভিসকে Node-এর একটি নির্দিষ্ট পোর্টে এক্সপোজ করে।
     - **LoadBalancer**: ক্লাউড-প্রোভাইডার-নির্ভর লোড ব্যালান্সার ব্যবহার করে।

---

### `**Type of Services in Kubernetes:**`

- **ClusterIP** (default): Pods-এর জন্য একটি স্থায়ী IP তৈরি করে, যা ক্লাস্টারের ভিতরে অ্যাক্সেস করা যায়।
- **NodePort**: সার্ভিসকে নোডের একটি নির্দিষ্ট পোর্টে এক্সপোজ করে, যা ক্লাস্টারের বাইরে থেকে অ্যাক্সেস করা যায়।
- **LoadBalancer**: ক্লাউড-প্রোভাইডার ভিত্তিক লোড ব্যালান্সার তৈরি করে।

এটি নিশ্চিত করে যে Pod-এর IP পরিবর্তিত হলেও, **Service** ব্যবহার করে অ্যাপ্লিকেশন সর্বদা অ্যাক্সেসযোগ্য থাকবে।



<br>
<br>
<br>


#  `#1.6 Manual Scheduling in kubernetes:  `

<br>
<br>
<br>


### **Manual Scheduling in Kubernetes with Labels and Selectors in Deployment YAML File**

Kubernetes-এ **manual scheduling** ব্যবহার করে আপনি নির্দিষ্ট **Node**-এ **Pod** বা **Deployment** চালাতে পারেন। আমরা **labels** এবং **selectors** ব্যবহার করে এটি কার্যকর করতে পারি। এবার আমরা আলোচনা করবো কীভাবে এটি Deployment-এ প্রয়োগ করা যায় এবং বিস্তারিতভাবে ব্যাখ্যা করবো।

---

### **Labels এবং Selectors-এর কাজ**
1. **Labels**:  
   - এটি একটি **key-value pair**, যা Kubernetes এর resources (যেমন Pod, Node, Deployment) কে চিহ্নিত করতে ব্যবহার করা হয়।  
   - উদাহরণ: 
     ```yaml
     labels:
       nodeType: high-memory
     ```

2. **Selectors**:  
   - এটি এমন একটি শর্ত যা **labels**-কে ফিল্টার করার জন্য ব্যবহৃত হয়।  
   - **nodeSelector** এর মাধ্যমে Pod শুধুমাত্র নির্দিষ্ট লেবেলযুক্ত Node-এ চলবে।  
   - উদাহরণ:
     ```yaml
     nodeSelector:
       nodeType: high-memory
     ```

---

### **কেন Manual Scheduling দরকার?**
- নির্দিষ্ট **Node**-এ গুরুত্বপূর্ণ অ্যাপ্লিকেশন স্থাপন করতে।
- **Resource optimization** নিশ্চিত করতে।
- **Production** এবং **development** পরিবেশ আলাদা রাখতে।

---

### **Deployment YAML File-এ Manual Scheduling**

#### **ধাপ-১: Node-এ Label যোগ করুন**
প্রথমে আপনার Node-এ একটি label সেট করুন।  
```bash
kubectl label nodes <node-name> nodeType=high-memory
```

#### **ধাপ-২: Deployment YAML File লিখুন**
এখন একটি Deployment তৈরি করুন এবং এতে **nodeSelector** ব্যবহার করুন।

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: nginx
        image: nginx
      nodeSelector:
        nodeType: high-memory  # শুধুমাত্র high-memory লেবেল সহ Node-এ যাবে
```

---

### **উদাহরণ বিশ্লেষণ**

1. **nodeSelector:**
   - এই অংশটি Deployment-কে নির্দেশ দেয় যে এটি শুধুমাত্র **nodeType=high-memory** লেবেলযুক্ত Node-এ Pods তৈরি করবে।
   
2. **replicas:**
   - `replicas: 3` এর অর্থ, Kubernetes একই Node-এ বা বিভিন্ন Nodes-এ ৩টি Pod তৈরি করবে।

3. **labels:**
   - Pod-গুলোর মধ্যে `app: my-app` লেবেল থাকবে, যা সেগুলোকে সহজে চিহ্নিত করতে সাহায্য করে।

---

### **ধাপ-৩: YAML ফাইল প্রয়োগ করুন**
Deployment ফাইলটি অ্যাপ্লাই করুন:
```bash
kubectl apply -f deployment.yml
```

#### **Pod-গুলো কোন Node-এ চলেছে তা দেখুন:**
```bash
kubectl get pods -o wide
```

---

### **Labels এবং Selectors-এর সুবিধা**
1. নির্দিষ্ট কাজের জন্য নির্দিষ্ট Node বরাদ্দ করতে সাহায্য করে।  
2. Resources ব্যবস্থাপনা সহজ হয়।  
3. Production এবং Development পরিবেশ আলাদা রাখা যায়।  

---

### **Deployment YAML File-এর সম্পূর্ণ উদাহরণ**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-scheduled-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: nginx
      nodeSelector:
        environment: production
```

#### **কীভাবে কাজ করবে:**
1. **nodeSelector** এর মাধ্যমে Pod-গুলো শুধুমাত্র `environment: production` লেবেলযুক্ত Node-এ চলবে।
2. দুইটি Pod তৈরি হবে, কারণ `replicas: 2` সেট করা আছে।

---

### **সারসংক্ষেপ**
- **Labels** এবং **nodeSelector** ব্যবহার করে Deployment YAML ফাইলের মাধ্যমে নির্দিষ্ট Node-এ Pods চালানো যায়।  
- এটি **resource optimization** এবং **application isolation** নিশ্চিত করতে সাহায্য করে।  
- **kubectl label nodes** কমান্ড দিয়ে Node-এ label যোগ করতে হয় এবং Deployment ফাইলে **nodeSelector** দিয়ে সেটি প্রয়োগ করা হয়।  

**এই পদ্ধতি Kubernetes-এ workload scheduling আরও নিয়ন্ত্রিত ও কার্যকর করে তোলে।**


