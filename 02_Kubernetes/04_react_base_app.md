
<br>
<br>

# `#4. Create a react base app and perform Operation: `

<br>
<br>


### **4.1 create node js api:**
```bash
npx create-react-app testapp
```

### **4.2 create docker file inside testapp**
```Dockerfile
# my node version is 23 "node -version"
FROM node:23

WORKDIR /myapp

COPY . . 

RUN npm install

EXPOSE 3000

CMD [ "npm", "start" ]

```

### **4.3 Now, let's create a image of this application:**


#### `আমরা যদি একটা docker image তৈরি করি তারপর সেই image কে লোকাল কম্পিউটার থেকে আমরা kubernetes pull করতে পারবো না । আমাদের এর জন্য docker image কে dockerhub এ upload করতে হবে । তারপর আমরা সেই dockerhub এর image কে  kubernetes এ pull করবো । `


### Let's go through the process:


### `**4.3.1. Create a Simple Node.js API: **`
Let’s set up a basic Node.js API using **Express**.

#### **Project Structure:**
```
node-api/
├── Dockerfile
├── index.js
├── package.json
└── deployment.yaml
```

### `**4.3.2. Create a Dockerfile:**`
```dockerfile
# Use the official Node.js image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the application files
COPY . .

# Expose the port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
```

### `**4.3.3. Build the Docker Image:**`

First, we will create docker repository. for that repo we will find `yourusername/node-api:latest`
t means tags that we see in our docker repository.

```bash
docker build -t yourusername/node-api:latest .
```
Replace `yourusername` with your Docker Hub username.


### `**4.3.4. Check All the Docker Images:**`

```bash
docker images
```

### **4.3.5. Push the Docker Image to Docker Hub**
Log in to Docker Hub:

```bash
docker login
```

Push the image:

```bash
docker push yourusername/node-api:latest
```


### `**4.3.6. Deploy the API to Kubernetes**`

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
`port binding করতে হবে: `

**first:**
```bash
kubectl expose deployment my-nginx --type=LoadBalancer --port=3000
```

**second:**
```bash
 kubectl get services 
```

**third:**
```bash
minikube service my-web-app 
```

# `#4.7 কীভাবে আমরা external port and Internal Port: বের করবো ?  `

<br>

## `#4.7.1 External Port Manage করা হয়ঃ LoadBalancer দিয়ে ঃ `

আমরা যখন একটা Deployment-কে `LoadBalancer` টাইপের সার্ভিস দিয়ে এক্সপোজ করেন, Kubernetes একটি ডিফল্ট **NodePort** নির্বাচন করে, যদি আমরা সেইটা স্পেসিফিক্যালি সেট না করি । এই NodePort এবং Cluster IP-এর মাধ্যমে আপনি সার্ভিস অ্যাক্সেস করতে পারেন।

### **কমান্ড দিয়ে সার্ভিসের বিস্তারিত তথ্য চেক করা**
```bash
kubectl get service my-web-app -o wide
```

#### **উদাহরণ আউটপুট:**
```
NAME          TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
my-web-app    LoadBalancer   10.96.159.232    <pending>     3000:32000/TCP   5m
```

- **PORT(S):** `3000:32000/TCP` — এটি নির্দেশ করে:
  - **Port (3000):** আপনার সার্ভিসের নির্দিষ্ট পোর্ট।
  - **NodePort (32000):** Kubernetes দ্বারা নির্ধারিত NodePort। আপনি এটি লোকালহোস্ট বা Minikube IP দিয়ে অ্যাক্সেস করতে পারেন।

### **Minikube ব্যবহার করলে**
Minikube-এ `LoadBalancer` সার্ভিসের জন্য IP খুঁজতে:
```bash
minikube service my-web-app --url
```

#### **উদাহরণ আউটপুট:**
```
http://192.168.49.2:32000
```

এটি ব্রাউজারে খুলে অ্যাপ্লিকেশনটি দেখতে পারবো । 

### **ক্লাস্টারের বাইরে থেকে অ্যাক্সেস করার জন্য (Production Cloud Environment)**
ক্লাউড পরিবেশে (যেমন GKE, EKS, AKS) `EXTERNAL-IP` ফিল্ড পূর্ণ হয়ে গেলে, সেটি ব্যবহার করতে পারেন:
```bash
kubectl get service my-web-app
```

#### আউটপুট:
```
NAME          TYPE           CLUSTER-IP       EXTERNAL-IP      PORT(S)        AGE
my-web-app    LoadBalancer   10.96.159.232    35.185.102.123   3000:32000/TCP 10m
```

এখানে `EXTERNAL-IP` (যেমন `35.185.102.123`) দিয়ে ব্রাউজারে `http://35.185.102.123:3000` খুলে অ্যাক্সেস করতে পারবেন।

### সারসংক্ষেপ:
1. **NodePort খুঁজতে:** `kubectl get service my-web-app -o wide`
2. **Minikube IP খুঁজতে:** `minikube service my-web-app --url`
3. **Cloud Environment এ IP খুঁজতে:** `kubectl get service my-web-app`



