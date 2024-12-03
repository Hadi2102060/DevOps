
<br>
<br>

# `#1 1st we will make the ip address static: `


# `#1.1 `ip link` command `

<br>
<br>

```bash
 ip link     

```


```css
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp0s31f6: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN mode DEFAULT group default qlen 1000
    link/ether d4:81:d7:75:be:dd brd ff:ff:ff:ff:ff:ff
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
    link/ether f4:8c:50:63:2a:09 brd ff:ff:ff:ff:ff:ff
4: br-6ce8302fc1a6: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default 
    link/ether 02:42:27:92:31:08 brd ff:ff:ff:ff:ff:ff
5: br-94bb7a7d4a45: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default 
    link/ether 02:42:3b:27:f3:fd brd ff:ff:ff:ff:ff:ff
6: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default 
    link/ether 02:42:4d:14:92:58 brd ff:ff:ff:ff:ff:ff
```


`ip link` কমান্ডটি লিনাক্সে নেটওয়ার্ক ইন্টারফেসের তথ্য দেখানোর জন্য ব্যবহৃত হয়।
---

### **1: lo: <LOOPBACK,UP,LOWER_UP>**
- **`lo`**: এটি "লুপব্যাক" ইন্টারফেস। এটি আপনার নিজের মেশিনের সাথে যোগাযোগের জন্য ব্যবহৃত হয়। এটি ইন্টারনালি ডেটা প্যাকেট প্রেরণ এবং গ্রহণ করে।
- **`<LOOPBACK,UP,LOWER_UP>`**: 
  - `LOOPBACK`: এটি একটি লুপব্যাক ডিভাইস।
  - `UP`: এটি সক্রিয় বা চালু আছে।
  - `LOWER_UP`: ফিজিক্যাল লেভেলেও এটি কাজ করছে।
  
---

<br>
<br>
<br>

---

## `লুপব্যাক (Loopback) কী?`
### **লুপব্যাক (Loopback) কী?**

লুপব্যাক ইন্টারফেস হলো কম্পিউটারের এমন একটা অংশ যেটা নিজের সাথে কথা বলে। ধরো, তুমি একা খেলছ, আর তুমি নিজে নিজের সাথে কথা বলছ—ঠিক সেরকম! 😄

---

### **কেন লুপব্যাক দরকার?**

1. **নিজের সাথে কথা বলা:**  
   ধরো, তোমার খেলনা গাড়িটা ঠিকমতো চলছে কিনা পরীক্ষা করতে হবে। তুমি গাড়িটাকে একটু ঠেলে দাও, আর দেখো সেটা ঠিকমতো ফিরে আসছে কিনা। লুপব্যাকও ঠিক তেমন! কম্পিউটার নিজের সাথে কথা বলে দেখে, "আমার ভেতরের জিনিসগুলো ঠিকঠাক কাজ করছে কিনা।"

---

### **লুপব্যাক কীভাবে কাজ করে?**

1. **একটা বিশেষ ঠিকানা আছে:**  
   ধরো, তোমার একটা "গোপন ঠিকানা" আছে, যেখানে তুমি চিঠি পাঠাও, কিন্তু সেটা শুধু তোমারই! কম্পিউটারে এই গোপন ঠিকানাটা হলো **127.0.0.1**, আর সবাই এটাকে বলে **localhost**। মানে, এটা কম্পিউটারের নিজের ঠিকানা।

2. **নিজের খেলনাগুলো পরীক্ষা করা:**  
   যেমন তুমি তোমার খেলনা পরীক্ষা করো, কম্পিউটারও এর ভেতরের সার্ভার (যেমন ওয়েবসাইট, অ্যাপ) ঠিকঠাক চলছে কিনা, সেটা পরীক্ষা করে।

---

### **উদাহরণ দিই:**  
ধরো, তোমার কম্পিউটার একটা ছোট্ট দোকানের মতো। আর দোকানের মালিক নিজের দোকানে এসে দেখে সব ঠিকঠাক আছে কিনা। কম্পিউটার এটা করার জন্য লুপব্যাক ইন্টারফেস ব্যবহার করে।

---

### **মজার ব্যাপার:**

- যদি তুমি টাইপ করো:
  ```bash
  ping 127.0.0.1
  ```
  কম্পিউটার বলবে, "হ্যাঁ, আমি ঠিক আছি, আমার নিজের সাথে যোগাযোগ করতে পারছি!" 🎉

---

### **লুপব্যাক ছাড়া কী হতো?**  
- ধরো, তোমার খেলনা পরীক্ষা করার জন্য তোমাকে বাইরে যেতে হতো। এতে অনেক সময় লাগত, আর ঝুঁকি থাকত।  
  কিন্তু লুপব্যাক কম্পিউটারকে বলে, "তুমি নিজের খেলনা ঘরেই পরীক্ষা করো।"

---

### **ছোট্ট সারাংশ:**
লুপব্যাক হলো কম্পিউটারের নিজের সাথে কথা বলার পদ্ধতি। এটা খুব সহজ এবং নিরাপদ, যেমন তুমি নিজের সাথে খেলতে পারো, তেমনি কম্পিউটারও নিজের জিনিস পরীক্ষা করতে পারে। 😄
---
<br>
<br>
<br>

### **mtu 65536**
- **`mtu`**: Maximum Transmission Unit বা সর্বোচ্চ ডেটা প্যাকেটের সাইজ যা এই ইন্টারফেসের মাধ্যমে প্রেরণ করা যেতে পারে। এখানে এটি 65536 বাইট।

---

### **qdisc noqueue state UNKNOWN**
- **`qdisc`**: Queue Discipline, এটি ইন্টারফেসের জন্য ট্র্যাফিক কন্ট্রোল পলিসি দেখায়। `noqueue` মানে কোনো ট্র্যাফিক ম্যানেজমেন্ট প্রয়োজন নেই।
- **`state UNKNOWN`**: ইন্টারফেসের বর্তমান স্টেট অজানা। এটি সাধারণত লুপব্যাক ইন্টারফেসে দেখা যায়।

---

### **mode DEFAULT group default qlen 1000**
- **`mode DEFAULT`**: এটি ডিফল্ট মোডে চলছে।
- **`group default`**: এটি ডিফল্ট গ্রুপে অন্তর্ভুক্ত।
- **`qlen 1000`**: ইন্টারফেসে 1000 প্যাকেটের একটি কিউ (লাইন) ধরে রাখতে পারে।

---

### **link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00**
- **`link/loopback`**: এটি লুপব্যাক লিংক নির্দেশ করে।
- **`00:00:00:00:00:00`**: লুপব্যাকের ম্যাক অ্যাড্রেস। এটি একটি স্ট্যান্ডার্ড ঠিকানা এবং পরিবর্তন হয় না।
- **`brd 00:00:00:00:00:00`**: ব্রডকাস্ট ঠিকানা, যা এখানে লুপব্যাক ইন্টারফেসের জন্য অপরিবর্তিত থাকে।

---

### **2: enp0s31f6: <NO-CARRIER,BROADCAST,MULTICAST,UP>**
- **`enp0s31f6`**: এটি আপনার মেশিনের তারযুক্ত ইথারনেট নেটওয়ার্ক ইন্টারফেস।
- **`<NO-CARRIER,BROADCAST,MULTICAST,UP>`**:
  - `NO-CARRIER`: ফিজিক্যালি কোনো তার (ক্যাবল) যুক্ত নেই।
  - `BROADCAST`: এটি ব্রডকাস্ট প্যাকেট পাঠাতে এবং গ্রহণ করতে সক্ষম।
  - `MULTICAST`: এটি মাল্টিকাস্ট প্যাকেট হ্যান্ডেল করতে পারে।
  - `UP`: ইন্টারফেসটি চালু আছে।

---

### **mtu 1500**
- **`mtu`**: এই ইন্টারফেসের সর্বোচ্চ প্যাকেট সাইজ 1500 বাইট।

---

### **qdisc fq_codel state DOWN mode DEFAULT group default qlen 1000**
- **`qdisc fq_codel`**: ট্র্যাফিক কন্ট্রোল পলিসি হলো "Fair Queuing Controlled Delay," যা লেটেন্সি কমানোর জন্য ব্যবহৃত হয়।
- **`state DOWN`**: ইন্টারফেসটি বর্তমানে বন্ধ বা অক্ষম।
  
---

### **link/ether d4:81:d7:75:be:dd brd ff:ff:ff:ff:ff:ff**
- **`link/ether`**: এটি ইথারনেট লিংক নির্দেশ করে।
- **`d4:81:d7:75:be:dd`**: ইন্টারফেসের ম্যাক অ্যাড্রেস।
- **`brd ff:ff:ff:ff:ff:ff`**: ইথারনেট ব্রডকাস্ট ঠিকানা, যা একটি নেটওয়ার্কে সকল ডিভাইসের জন্য প্রযোজ্য।

---

### **3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP>**
- **`wlan0`**: এটি আপনার ওয়াইফাই নেটওয়ার্ক ইন্টারফেস।
- **`<BROADCAST,MULTICAST,UP,LOWER_UP>`**:
  - `BROADCAST` এবং `MULTICAST`: এটি ব্রডকাস্ট এবং মাল্টিকাস্ট প্যাকেট হ্যান্ডেল করতে সক্ষম।
  - `UP`: ইন্টারফেসটি চালু।
  - `LOWER_UP`: এটি সঠিকভাবে সংযুক্ত এবং কাজ করছে।

---

### **mtu 1500**
- ওয়াইফাই ইন্টারফেসের সর্বোচ্চ প্যাকেট সাইজ 1500 বাইট।

---

### **qdisc noqueue state UP mode DORMANT group default qlen 1000**
- **`state UP`**: ইন্টারফেসটি সক্রিয়।
- **`mode DORMANT`**: এটি বর্তমানে নেটওয়ার্ক ট্রাফিক আদান-প্রদান করছে না।

---

### **link/ether f4:8c:50:63:2a:09 brd ff:ff:ff:ff:ff:ff**
- **`link/ether`**: এটি ইথারনেট টাইপ লিংক নির্দেশ করে।
- **`f4:8c:50:63:2a:09`**: ওয়াইফাই ইন্টারফেসের ম্যাক অ্যাড্রেস।
- **`brd ff:ff:ff:ff:ff:ff`**: ব্রডকাস্ট ঠিকানা।

---

### **4, 5, 6: br-... এবং docker0**
- এগুলো Docker দ্বারা তৈরি ভার্চুয়াল নেটওয়ার্ক ব্রিজ। এগুলি মূলত Docker কন্টেইনারের মধ্যে যোগাযোগ পরিচালনার জন্য ব্যবহৃত হয়।
- **`NO-CARRIER`**: এগুলো কোনো ফিজিক্যাল ডিভাইসের সাথে সংযুক্ত নয়, তাই কোনো ক্যারিয়ার নেই।
- **`state DOWN`**: এগুলো বর্তমানে অক্ষম।

---
---
---

<br>
<br>

# `#1.2 `ip addr` command:`

<br>
<br>

---
---
---

```bash
ip addr                     
```

```css
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: enp0s31f6: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether d4:81:d7:75:be:dd brd ff:ff:ff:ff:ff:ff
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether f4:8c:50:63:2a:09 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.114/24 brd 192.168.0.255 scope global dynamic noprefixroute wlan0
       valid_lft 5873sec preferred_lft 5873sec
    inet6 fe80::ba1:c0f1:9b01:e9a/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
4: br-6ce8302fc1a6: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:27:92:31:08 brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-6ce8302fc1a6
       valid_lft forever preferred_lft forever
5: br-94bb7a7d4a45: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:3b:27:f3:fd brd ff:ff:ff:ff:ff:ff
    inet 192.168.49.1/24 brd 192.168.49.255 scope global br-94bb7a7d4a45
       valid_lft forever preferred_lft forever
6: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:4d:14:92:58 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
```

---
---
---

# `# **IPv4** এবং **IPv6** এর মধ্যে পার্থক্য:`

### **1. IPv4 (Internet Protocol Version 4):**  
- **সংখ্যা দিয়ে কাজ করে।**  
  - উদাহরণ: `192.168.0.1`  
- **ঠিকানার দৈর্ঘ্য:** ৩২-বিট।  
  - এটি ৪টি সংখ্যা দিয়ে গঠিত, প্রতিটি সংখ্যা ০ থেকে ২৫৫ পর্যন্ত।  
- **ঠিকানার সংখ্যা:**  
  - ৪.৩ বিলিয়ন (৪৩০ কোটি) ঠিকানা দিতে পারে।  
  - বর্তমান বিশ্বে কম্পিউটার ও ডিভাইস অনেক বেড়ে যাওয়ায় IPv4 ঠিকানা প্রায় শেষ।  
- **নোটেশন (লিখার ধরণ):**  
  - ডট (.) দিয়ে আলাদা করা হয়।  
  - উদাহরণ: `192.168.1.1`।  
- **ব্যবহার:**  
  - পুরনো ইন্টারনেট সিস্টেম এবং বেশিরভাগ ডিভাইসে।  
- **নিরাপত্তা:**  
  - IPv4 তে বিল্ট-ইন সিকিউরিটি সিস্টেম নেই। আলাদাভাবে সিকিউরিটি যোগ করতে হয়।  
- **বাধা:**  
  - ঠিকানার সংখ্যা সীমিত এবং ধীরে ধীরে এটি অপ্রতুল হয়ে উঠছে।

---

### **2. IPv6 (Internet Protocol Version 6):**  
- **সংখ্যা এবং অক্ষর দিয়ে কাজ করে।**  
  - উদাহরণ: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`  
- **ঠিকানার দৈর্ঘ্য:** ১২৮-বিট।  
  - এটি সংখ্যা এবং হেক্সাডেসিমাল অক্ষর (0-9, a-f) দিয়ে গঠিত।  
- **ঠিকানার সংখ্যা:**  
  - তাত্ত্বিকভাবে আনলিমিটেড (৩৪০ আনডেসিলিয়ন ঠিকানা)।  
  - সহজ কথায়, এত ঠিকানা আছে যে তা কখনোই শেষ হবে না।  
- **নোটেশন (লিখার ধরণ):**  
  - কোলন (:) দিয়ে আলাদা করা হয়।  
  - উদাহরণ: `2001:db8::1`।  
- **ব্যবহার:**  
  - নতুন ইন্টারনেট সিস্টেম এবং উন্নত ডিভাইসে।  
- **নিরাপত্তা:**  
  - IPv6 এ বিল্ট-ইন সিকিউরিটি ব্যবস্থা আছে (IPSec)।  
- **উন্নতি:**  
  - দ্রুত ডেটা ট্রান্সমিশন এবং ভবিষ্যতের জন্য প্রস্তুত।

---

### **কেন IPv6 প্রয়োজন?**  
বিশ্বে ইন্টারনেট-যুক্ত ডিভাইসের সংখ্যা প্রতিদিন বাড়ছে। স্মার্টফোন, স্মার্টওয়াচ, টিভি, গাড়ি—সবকিছুই ইন্টারনেট ব্যবহার করছে। IPv4 দিয়ে এই চাহিদা মেটানো সম্ভব নয়। এজন্য IPv6 নিয়ে আসা হয়েছে।  

---
---
---

<br>
<br>
<br>

---

### **1: `lo` (লুপব্যাক ইন্টারফেস)**

- **লুপব্যাক ইন্টারফেস কি?**  
  - এটি এমন একটি ইন্টারফেস যা কম্পিউটার নিজেই নিজের সাথে যোগাযোগ করার জন্য ব্যবহার করে।  
  - আপনি যখন `127.0.0.1` বা `localhost` ব্যবহার করেন, তখন এই ইন্টারফেস কাজ করে।  

- **ব্যাখ্যা:**  
  - **`lo:`** এটি লুপব্যাক ইন্টারফেসের নাম।  
  - **`<LOOPBACK,UP,LOWER_UP>`:** এটি বলে দিচ্ছে যে এই ইন্টারফেসটি সক্রিয় (UP) এবং কাজ করছে।  
  - **`mtu 65536:`** এটি বলে দিচ্ছে লুপব্যাক ইন্টারফেস একবারে সর্বোচ্চ ৬৫,৫৩৬ বাইট ডেটা পাঠাতে বা গ্রহণ করতে পারে।  
  - **`inet 127.0.0.1/8:`**  
    - এটি লুপব্যাক ইন্টারফেসের IPv4 ঠিকানা।  
    - `127.0.0.1` মানে আপনার কম্পিউটার নিজেই নিজের সাথে যোগাযোগ করছে।  
  - **`inet6 ::1/128:`**  
    - এটি লুপব্যাক ইন্টারফেসের IPv6 ঠিকানা।  
    - `::1` IPv6 এ লুপব্যাকের সমান।

---

### **2: `enp0s31f6` (ইথারনেট ইন্টারফেস)**

- **ইথারনেট ইন্টারফেস কি?**  
  - এটি একটি ফিজিক্যাল নেটওয়ার্ক পোর্ট (যেমন ল্যাপটপে থাকা কেবল সংযোগ দেওয়ার পোর্ট)।

- **ব্যাখ্যা:**  
  - **`enp0s31f6:`** এটি ইথারনেট ইন্টারফেসের নাম।  
  - **`<NO-CARRIER,UP>`:** এটি বলছে যে ইন্টারফেস সক্রিয় (UP) কিন্তু কোনো ক্যাবল সংযোগ নেই (NO-CARRIER)।  
  - **`link/ether d4:81:d7:75:be:dd:`**  
    - এটি ইন্টারফেসের MAC ঠিকানা।  
    - MAC ঠিকানা মানে, ইন্টারফেসের ইউনিক হার্ডওয়্যার আইডি।  

---

### **3: `wlan0` (ওয়াই-ফাই ইন্টারফেস)**

- **ওয়াই-ফাই ইন্টারফেস কি?**  
  - এটি আপনার কম্পিউটারের ওয়াই-ফাই ব্যবহার করার জন্য দায়ী।  

- **ব্যাখ্যা:**  
  - **`wlan0:`** এটি ওয়াই-ফাই ইন্টারফেসের নাম।  
  - **`<UP,LOWER_UP>`:** এটি সক্রিয় এবং কাজ করছে।  
  - **`inet 192.168.0.114/24:`**  
    - এটি আপনার ওয়াই-ফাই থেকে প্রাপ্ত IPv4 ঠিকানা।  
    - `192.168.0.114` হলো আপনার ডিভাইসের ঠিকানা।  
  - **`inet6 fe80::ba1:c0f1:9b01:e9a/64:`**  
    - এটি ওয়াই-ফাই এর IPv6 ঠিকানা।  

---

### **4: `br-6ce8302fc1a6` (ডকার ব্রিজ)**

- **ডকার ব্রিজ কি?**  
  - এটি একটি ভার্চুয়াল নেটওয়ার্ক, যা ডকার কন্টেইনারগুলোর মধ্যে যোগাযোগ করার জন্য ব্যবহৃত হয়।  

- **ব্যাখ্যা:**  
  - **`br-6ce8302fc1a6:`** এটি ডকার তৈরি করা একটি ভার্চুয়াল ব্রিজের নাম।  
  - **`inet 172.18.0.1/16:`**  
    - এটি ব্রিজের IPv4 ঠিকানা।  

---

### **5: `docker0` (ডকারের ডিফল্ট ব্রিজ)**

- **ডকার ব্রিজ কি?**  
  - এটি ডকার কন্টেইনারগুলোর জন্য একটি ডিফল্ট নেটওয়ার্ক।  

- **ব্যাখ্যা:**  
  - **`docker0:`** এটি ডকারের ডিফল্ট ব্রিজের নাম।  
  - **`inet 172.17.0.1/16:`**  
    - এটি ডকার ব্রিজের IPv4 ঠিকানা।  

---

### সহজ ভাষায় গুরুত্বপূর্ণ বিষয়:

1. **লুপব্যাক (lo):**  
   - কম্পিউটার নিজের সাথে কথা বলে।  

2. **ইথারনেট (enp0s31f6):**  
   - কেবল দিয়ে নেটওয়ার্কে সংযোগের জন্য।  

3. **ওয়াই-ফাই (wlan0):**  
   - ওয়াই-ফাই দিয়ে নেটওয়ার্কে সংযোগের জন্য।  

4. **ডকার ব্রিজ:**  
   - ভার্চুয়াল নেটওয়ার্ক, যা ডকার ব্যবহার করে।  

---
---

<br>
<br>

# `#1.3: Ip Address, Subnet Mask, GateWay,DNS কী? `

<br>
<br>

---
---
---

### **১. IP ঠিকানা (IP Address)**  
**IP ঠিকানা** হলো তোমার কম্পিউটারের একক পরিচয়। এটি তোমার কম্পিউটারের **ঠিকানা** হিসেবে কাজ করে, যাতে নেটওয়ার্কে অন্য ডিভাইসগুলো তোমাকে খুঁজে পায়।  

#### **বাস্তব উদাহরণ:**  
- তোমার কম্পিউটারের **IP:** `192.168.0.114`।  
- যখন তুমি ইন্টারনেটে কিছু ব্রাউজ করো, তোমার ডিভাইস এই ঠিকানার মাধ্যমেই ডেটা পাঠায় এবং গ্রহণ করে।

---

### **২. সাবনেট মাস্ক (Subnet Mask)**  
**সাবনেট মাস্ক** হলো একটা নিয়ম, যা বলে দেয় তোমার কম্পিউটার কোন নেটওয়ার্কের অংশ।  
এটি IP ঠিকানার **নেটওয়ার্ক** এবং **ডিভাইস** অংশ আলাদা করতে সাহায্য করে।  

#### **বাস্তব উদাহরণ:**  
- **সাবনেট মাস্ক:** `255.255.255.0`  
- যদি তোমার IP ঠিকানা `192.168.0.114` হয়, তাহলে:  
  - **নেটওয়ার্ক অংশ:** `192.168.0`  
  - **ডিভাইস অংশ:** `114`  
  এতে একই নেটওয়ার্কে থাকা সব ডিভাইস সহজে যোগাযোগ করতে পারে।  

---

### **৩. গেটওয়ে (Gateway)**  
**গেটওয়ে** হলো নেটওয়ার্কের বাইরে যাওয়ার দরজা।  
তোমার কম্পিউটার লোকাল নেটওয়ার্কের বাইরে (ইন্টারনেটে) ডেটা পাঠাতে এবং আনতে **গেটওয়ে** ব্যবহার করে।  

#### **বাস্তব উদাহরণ:**  
- তোমার গেটওয়ে ঠিকানা সাধারণত তোমার রাউটারের ঠিকানা হয়।  
- **গেটওয়ে ঠিকানা:** `192.168.0.1`  
  এটি তোমার লোকাল নেটওয়ার্ককে ইন্টারনেটের সাথে সংযুক্ত করে।  

---

### **৪. DNS (Domain Name System)**  
**DNS** হলো ইন্টারনেটের ঠিকানাগুলো খুঁজে পাওয়ার সিস্টেম।  
তুমি যখন **`google.com`** লিখো, তখন DNS সার্ভার সেটা একটা **IP ঠিকানায়** (যেমন: `142.250.190.46`) রূপান্তর করে।  

#### **বাস্তব উদাহরণ:**  
- DNS সার্ভার ঠিকানা হলো:  
  - **প্রথম DNS:** `8.8.8.8` (গুগলের পাবলিক DNS)  
  - **দ্বিতীয় DNS:** `8.8.4.4`  

---

### **বাস্তব চিত্র:**  
ধরো, তোমার বাসায় ইন্টারনেট আছে। এভাবে কাজ হবে:  
1. **IP ঠিকানা:** `192.168.0.114` → তোমার কম্পিউটারের ঠিকানা।  
2. **সাবনেট মাস্ক:** `255.255.255.0` → তোমার নেটওয়ার্কের অন্যান্য ডিভাইস চিনতে সাহায্য করে।  
3. **গেটওয়ে:** `192.168.0.1` → তোমার রাউটার, যা ইন্টারনেটের সাথে যোগাযোগ করে।  
4. **DNS:** `8.8.8.8` → নাম থেকে IP খুঁজে বের করে।  

### **এগুলো কিভাবে ব্যবহার হয়?**  
#### **১. IP ঠিকানা:**  
- এটা দিয়ে জানাবে তোমার ডিভাইস কোথায়।  
- অন্য ডিভাইস তোমাকে খুঁজে পাবে।  

#### **২. সাবনেট মাস্ক:**  
- তোমার নেটওয়ার্কের ভিতরে ডিভাইসগুলো চিনতে।  
- লোকাল নেটওয়ার্ক আলাদা রাখতে।  

#### **৩. গেটওয়ে:**  
- ইন্টারনেটে সংযোগ করতে।  
- লোকাল নেটওয়ার্কের বাইরে ডেটা পাঠাতে।  

#### **৪. DNS:**  
- তোমার দেওয়া নাম (যেমন: `google.com`) থেকে IP ঠিকানা খুঁজে বের করে।  

# `#1.4 Find all the value of: Ip address, Gateway, DNS server: `

### **Your Network Details:**

#### **1. IP Address**  
Your current **IP address** (for the active wireless interface `wlan0`):  
`192.168.0.114`

#### **2. Gateway**  
The gateway isn't explicitly shown in the `ip addr` command.  
To find it, use the command:  
```bash
ip route | grep default
```
This will return something like:  
```
default via 192.168.0.1 dev wlan0
```
Here, `192.168.0.1` would be your **gateway address**.

#### **3. DNS Server**  
To find your DNS server, check the contents of your `/etc/resolv.conf` file:  
```bash
cat /etc/resolv.conf
```
Typical DNS entries look like:  
```
nameserver 8.8.8.8
nameserver 8.8.4.4
```
If you're using a router, it might show the router's IP (e.g., `192.168.0.1`) as the DNS.

---
<br>
<br>
<br>
<br>

---
---
---

If your `/etc/systemd/network/` folder is empty, it means the `systemd-networkd` service isn't fully configured yet. Here's how you can set it up from scratch to assign a static IP to your `wlan0` interface:

---

### **Step 1: Create the Network Directory**
Ensure the directory exists:
```bash
sudo mkdir -p /etc/systemd/network/
```

---

### **Step 2: Create a Network Configuration File**
Create a file for your Wi-Fi interface:
```bash
sudo nano /etc/systemd/network/25-wifi.network
```

Add the following content to assign a static IP to `wlan0`:
```ini
[Match]
Name=wlan0  # Replace this if your Wi-Fi interface has a different name

[Network]
Address=192.168.1.100/24  # Replace with your desired static IP and subnet mask
Gateway=192.168.1.1       # Replace with your router's gateway
DNS=8.8.8.8               # Replace with your preferred DNS server
```

Save and exit.

---

### **Step 3: Enable `systemd-networkd`**
Ensure the `systemd-networkd` service is enabled and active:
```bash
sudo systemctl enable systemd-networkd
sudo systemctl restart systemd-networkd
```

---

### **Step 4: Enable DHCP for Wi-Fi (if needed)**
If you want to connect to Wi-Fi with `wpa_supplicant`:

1. **Install `wpa_supplicant` (if not already installed):**
   ```bash
   sudo pacman -S wpa_supplicant
   ```

2. **Create/Edit the `wpa_supplicant` Config File:**
   ```bash
   sudo nano /etc/wpa_supplicant/wpa_supplicant-wlan0.conf
   ```

   Add your Wi-Fi details:
   ```ini
   network={
       ssid="Your_SSID"
       psk="Your_PASSWORD"
   }
   ```

3. **Start and Enable `wpa_supplicant`:**
   ```bash
   sudo systemctl enable wpa_supplicant@wlan0
   sudo systemctl restart wpa_supplicant@wlan0
   ```

4. **Restart Your Networking Services:**
   ```bash
   sudo systemctl restart systemd-networkd
   ```

---

### **Step 5: Verify Configuration**
1. Check your IP address:
   ```bash
   ip addr show wlan0
   ```

2. Test the connection:
   ```bash
   ping 8.8.8.8
   ```

---

If you still face issues, confirm that:
1. Your `systemd-networkd` is running:
   ```bash
   sudo systemctl status systemd-networkd
   ```
2. Your Wi-Fi connection is active and associated with an access point:
   ```bash
   iw wlan0 link
   ```

   
