
<br>

---

<br>

# `#1. Multi container app in same POD`

<br>
<br>

---


`আমরা আগে দুইটা configuration ফাইল দেখেছিলাম কিন্তু আমরা এখন ১টা ফাইল দিয়েই সব কিছু করবো । এর জন্য আমরা --- use করবো, seperator হিসেবে । `



```yml

(depolyment file properties)

---

(services file properties)

```
<br>
<br>

# `#1.2 Run mongodb locally by the HELP of Docker: `


```bash
docker run -p 27017:27017 -d --name mongodb mongo
```

এটি একটি **MongoDB** কন্টেইনার চালু করবে Docker-এ। এই কমান্ডের প্রতিটি অংশের ব্যাখ্যা:

1. `docker run`: এটি Docker কন্টেইনার চালু করার জন্য ব্যবহার করা হয়।

2. `-p 27017:27017`: এটি কন্টেইনারের ভিতরের MongoDB পোর্ট (27017) কে আপনার হোস্ট মেশিনের পোর্ট (27017) এর সাথে ম্যাপ করে, যাতে আপনি হোস্ট মেশিনের মাধ্যমে MongoDB অ্যাক্সেস করতে পারেন।

3. `-d`: এটি কন্টেইনারটিকে ডিটাচড মোডে (ব্যাকগ্রাউন্ডে) চালু করে। অর্থাৎ কন্টেইনার চালু হওয়ার পর, আপনার টার্মিনাল আপনাকে ফিরিয়ে দেয় কন্টেইনারের আইডি, কিন্তু কন্টেইনারের লগ বা আউটপুট দেখতে পারবেন না।
4. `--name mongodb`: এটি কন্টেইনারের একটি নাম নির্ধারণ করে, যা এখানে `mongodb` দেওয়া হয়েছে।
5. `mongo`: এটি MongoDB Docker ইমেজটি ব্যবহার করবে কন্টেইনার চালানোর জন্য।

আপনার যে `916a8eb22f63af0dadd150bb01e80e4b3d6d3150e6f0ae19d01436437172db4c` কোডটি দেখাচ্ছে, সেটি হলো **কন্টেইনারের আইডি**। এটি একটি ইউনিক হ্যাশ যা Docker কন্টেইনারকে শনাক্ত করতে ব্যবহৃত হয়। যেহেতু আপনি `-d` ফ্ল্যাগ ব্যবহার করেছেন, তাই কন্টেইনারটি ব্যাকগ্রাউন্ডে চলে গেছে, এবং আপনার টার্মিনালে শুধুমাত্র কন্টেইনারের ID দেখানো হয়েছে।

এটি সহজভাবে বলতে গেলে, `916a8eb22f63af0dadd150bb01e80e4b3d6d3150e6f0ae19d01436437172db4c` হল কন্টেইনারের একটি বিশেষ চিহ্ন বা আইডি যা Docker এর মধ্যে ব্যবহার হয় কন্টেইনারের অবস্থান বা পরিস্থিতি ট্র্যাক করতে।

<br>
<br>

---
---

# `#1.3 আমরা যখন,kubernetes এ docker-> mongodb:latest image ব্যবহার করবো, তখন nodejs এ আমরা যে data use করবো সেইটা verify করবো কীবাভে, এর জন্য নিচের command ব্যবহার করবোঃ `

### **In Kubernetes (with `mongo` Container)**

If you are running MongoDB inside Kubernetes, execute the following steps:

1. **Access the MongoDB Shell in the Pod:**
   ```bash
   kubectl exec -it <mongo-pod-name> -c mongo -- mongo
   ```

2. **Switch to the New Database:**
   ```javascript
   use demoDatabase
   ```

3. **Create a Collection and Insert Data:**
   ```javascript
   db.demoCollection.insertOne({ name: "Kubernetes Demo", value: 42 })
   ```

4. **Verify the Database:**
   ```javascript
   show dbs
   ```

---
---

<br>
<br>


