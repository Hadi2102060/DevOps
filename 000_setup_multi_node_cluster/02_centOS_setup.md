<br>
<br>
<br>

# `# 01 Some important Concept :: `

<br>
<br>
<br>

### **SELinux (Security-Enhanced Linux) কি?**

SELinux হলো একটা সিকিউরিটি সিস্টেম, যা আপনার কম্পিউটারের ফাইল আর প্রোগ্রামগুলোকে সুরক্ষিত রাখে। এটা বলে দেয় কোন প্রোগ্রাম কী ধরনের কাজ করতে পারবে আর কোনটা পারবে না।  
উদাহরণ:  
তোমার ঘরে তিনটে ঘর আছে, কিন্তু একটায় তোমার চকলেট রাখা। SELinux ঠিক করবে কে কোন ঘরে ঢুকতে পারবে। 

**কেন বন্ধ করি?**  
Kubernetes-এ অনেক কাজের জন্য এটা বাধা দেয়, তাই একে বন্ধ করতে হয়।

---

### **`net.bridge.bridge-nf-call-ip6tables = 1` এবং `net.bridge.bridge-nf-call-iptables = 1` এর কাজ**

Kubernetes এর নেটওয়ার্ক সিস্টেম ঠিকমতো কাজ করার জন্য এই লাইনগুলো দরকার।  

- **`net.bridge.bridge-nf-call-ip6tables = 1`**  
  এটা বলে, IPv6 (ইন্টারনেট অ্যাড্রেসের আরেক ফরম্যাট) এর জন্য নেটওয়ার্ক প্যাকেটগুলো চেক করো।  

- **`net.bridge.bridge-nf-call-iptables = 1`**  
  এটা বলে, নেটওয়ার্কে যাওয়া আসা সব ডেটা (packet) চেক করো।

**কেন দরকার?**  
Kubernetes এর বিভিন্ন নোডের (মাস্টার-ওয়ার্কার) মধ্যে যোগাযোগ ঠিক রাখতে হলে এগুলো অন করতে হয়।

---

### **IP অ্যাড্রেস, নেটমাস্ক, গেটওয়ে, আর DNS কি?**

#### **1. IP অ্যাড্রেস (Internet Protocol Address):**  
তোমার কম্পিউটারের ঠিকানা।  
উদাহরণ: তোমার বাসার ঠিকানা যেমন "২ নং রাস্তা, ঢাকা," IP হলো কম্পিউটারের ঠিকানা, যেমন: `192.168.0.1`।

#### **2. নেটমাস্ক (Netmask):**  
বলে দেয়, নেটওয়ার্কে কতগুলো কম্পিউটার বা ডিভাইস থাকবে।  
উদাহরণ: তোমার পাড়ার মধ্যে কোন কোন বাসা একসাথে একটা গ্রুপে আছে, সেটা নেটমাস্ক ঠিক করে।

#### **3. গেটওয়ে (Gateway):**  
তোমার কম্পিউটার অন্য নেটওয়ার্কে যাওয়ার রাস্তা।  
উদাহরণ: তোমার পাড়ার বাইরের রাস্তায় যেতে দরজা বা গেট যেটা ব্যবহার করবে, সেটাই গেটওয়ে।

#### **4. DNS (Domain Name System):**  
ওয়েবসাইটের নাম মনে রাখা সহজ, কিন্তু কম্পিউটার আসলে IP অ্যাড্রেস দিয়ে কাজ করে। DNS নামগুলো IP-তে বদলে দেয়।  
উদাহরণ: তুমি "google.com" টাইপ করো, DNS জানে এর IP `142.250.190.78`।

---

### **সব কিছু একসাথে সহজভাবে:**
- **SELinux**: কম্পিউটারের দারোয়ান, কে কী করবে ঠিক করে।  
- **`net.bridge` লাইনগুলো**: Kubernetes এর নেটওয়ার্কে ডেটা ঠিক রাখতে সাহায্য করে।  
- **IP অ্যাড্রেস**: কম্পিউটারের নাম বা ঠিকানা।  
- **নেটমাস্ক**: নেটওয়ার্কের সীমানা ঠিক করে।  
- **গেটওয়ে**: বাইরে যাওয়ার রাস্তা।  
- **DNS**: ওয়েবসাইটের নাম থেকে IP খুঁজে দেয়।

<br>
<br>

---
---
---
---

<br>
<br>

# `# 02 Command: `

### Step-by-Step Explanation in Bengali for Kubernetes Multi-Node Cluster Setup on CentOS:

---

#### **Firewall বন্ধ করা**
```bash
systemctl disable firewalld
```
ফায়ারওয়াল (firewall) বন্ধ করে দিলাম, যাতে নেটওয়ার্ক সংক্রান্ত বাধা না হয়।

---

#### **মেমোরি চেক করা**
```bash
free -h
```
মেমোরি আর স্যাপ (swap) স্পেস কত আছে, সেটা দেখি।

---

#### **স্যাপ বন্ধ করা**
```bash
swapoff -a; sed -i '/swap/d' '/etc/fstab'
```
স্যাপ (swap) বন্ধ করলাম, যাতে Kubernetes কাজ করতে পারে। `/etc/fstab` থেকে স্যাপের লাইন মুছে দিলাম, যাতে স্যাপ রিবুটের সময়ও চালু না হয়।

---

#### **ফাইল চেক করা**
```bash
cat /etc/fstab
```
এখন চেক করলাম, ফাইলটায় স্যাপ সম্পর্কিত কিছু নেই।

---

#### **SELinux বন্ধ করা**
```bash
setenforce 0
```
SELinux বন্ধ করে দিলাম। এটা সিকিউরিটির জন্য ব্যবহার হয়, কিন্তু Kubernetes-এ সমস্যা করতে পারে।

```bash
getenforce
```
চেক করলাম, SELinux বন্ধ হয়েছে কি না।

```bash
sed -i --follow-symlinks 's/^SELINUX=enforcing/SELINUX=disabled/' /etc/sysconfig/selinux
```
এই লাইন দিয়ে SELinux পুরোপুরি বন্ধ করে দিলাম এবং এটা ফাইলেও আপডেট করলাম।

```bash
cat /etc/sysconfig/s
```
ফাইলটা খুলে দেখি সব ঠিকমতো হয়েছে কি না।

---

#### **কনফিগারেশন আপডেট করা**
```bash
vim /etc/sysctl.d/kubernetes.conf
```
এখন একটা নতুন ফাইল তৈরি করলাম এবং নিচের লাইনগুলো যোগ করলাম:
```
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
```
এগুলো Kubernetes-এর নেটওয়ার্ক সিস্টেমের জন্য দরকার।

```bash
sysctl --system
```
ফাইলের নতুন সেটিংসগুলো সিস্টেমে লোড করলাম।

---

#### **ডকার ইন্সটল করার প্রস্তুতি**
```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
```
ডকার ইন্সটল করতে কিছু দরকারি টুলস আগে ইন্সটল করলাম।

```bash
# যদি কোনো এরর হয়:
kill -9 PID_NUMBER
```
এরর হলে পিআইডি (PID) দিয়ে প্রসেস বন্ধ করতে হবে।

---

#### **ডকার-এর রিপোজিটরি যোগ করা**
```bash
yum-config-manager --add-repo https://download/docker.com/linux/centos/docker-ce.repo
```
ডকার ইন্সটল করার জন্য এর রিপোজিটরি (repo) সিস্টেমে যোগ করলাম।

```bash
cat (address_at_the_end_of_the_previous_command)
```
চেক করলাম, রিপোজিটরি ঠিকমতো যোগ হয়েছে কি না।

---

#### **ডকার ইন্সটল করা**
```bash
yum install -y docker-ce-19.03.12
```
ডকার ইন্সটল করলাম।

```bash
systemctl start docker
systemctl enable docker
systemctl status docker
```
ডকার চালু করলাম, যাতে রিবুটের পরেও এটা নিজে নিজে চালু থাকে। অবস্থা চেক করলাম।

---

#### **Git ইন্সটল করা**
```bash
yum install git -y
```
Git ইন্সটল করলাম।

```bash
git clone https://github/com/cloudcontainertech/k8spackages.git
```
কুবারনেটসের প্যাকেজ ডাউনলোড করার জন্য রিপোজিটরি ক্লোন করলাম।

```bash
ls -lrth
```
চেক করলাম, প্যাকেজগুলো ডাউনলোড হয়েছে।

---

#### **কুবারনেটস ডিরেক্টরিতে যাওয়া**
```bash
cd k8spackages/
ls -lrth
```
ডিরেক্টরির মধ্যে ঢুকে চেক করলাম, ফাইলগুলো ঠিকঠাক আছে।

---

#### **হোস্টনেম বদলানো**
```bash
hostnamectl set-hostname k8smaster.example.com
```
সিস্টেমের নাম দিলাম `k8smaster.example.com`।

```bash
bash
```
নতুন হোস্টনেম লোড করলাম।

---

#### **নেটওয়ার্ক কনফিগারেশন আপডেট করা**
```bash
vim /etc/sysconfig/network-scripts/ifcfg-ens33
```
ফাইলটা এডিট করে IP অ্যাড্রেস, নেটমাস্ক, গেটওয়ে, আর DNS আপডেট করলাম।

```bash
systemctl restart network
```
নেটওয়ার্ক রিস্টার্ট করলাম, যাতে পরিবর্তনগুলো কাজ করে।

---

#### **হোস্ট ফাইল আপডেট করা**
```bash
vim /etc/hosts
```
মাস্টার আর ওয়ার্কার নোডের IP অ্যাড্রেসগুলো যোগ করলাম।

---

#### **Kubernetes কুবলেট চালু করা**
```bash
systemctl enable kubelet.service
```
`kubelet` সার্ভিস চালু করলাম।

```bash
reboot
```
সিস্টেম রিবুট করলাম।

---

#### **মাস্টার নোড ইনিশিয়ালাইজ করা**
```bash
kubeadm init --apiserver-advertise-address=192.168.60.51 --pod-network-cidr=192.168.0.0/16
```
মাস্টার নোড শুরু করলাম। IP অ্যাড্রেস আর নেটওয়ার্ক রেঞ্জ সঠিকভাবে দিয়েছি।

---

