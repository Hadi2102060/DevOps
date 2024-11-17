
<br>

---
<br>

# `#10: YAML Configuration:) for deployment: `

<br>
<br>

---
---

`আমরা সবকিছু kubernetes এ add করার জন্য অনেক গুলো step follow করেছি । এখন, আমাদের কাছে যদি একটা configuration file থাকে তাহলে সবকিছু manage করতে সুবিধা হয় । এই configuration file yaml হবে । `

<br>

## `#10.1 1st let's create deployment configuration file: `
- `File Location does not matter.So, create a file named,  ---.yaml file.`
- `এরপর আমরা kubernetes এর থেকে nginx এর জন্য যে yaml file আছে সেইটা কপি করবো ।` 


```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  # Unique key of the Deployment instance
  name: my-express-demo
spec:
  # 3 Pods should exist at all times.
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        # Apply this label to pods and default
        # the Deployment label selector to this value
        app: nginx
    spec:
      containers:
      - name: nginx
        # Run this image
        image: nginx:1.14

```
### এখানে, 

- Group-> apps, Version->v1, type-> Deployment
- মেটাডেটাতে আমরা নাম দিব । যেমনটা deployment create করার সময় নাম দিয়েছিলামঃ `kubectl create deployment my-nginx --image=nginx:latest` here(my-nginx)
- replicas তো কয়টা instance হবে তার সংখ্যা । 
- selector: এটা একটু পরে দেখবো । 
-  template: (উপরের গুলো, deployment এর জন্য এখন আমরা template এ POD এর information দিব। )
    
    - template এর  metadata এর মধ্যে যেই labels আছে এখানে আমরা যেই নাম দিবো, সেম নাম আমরা spec এর selector এর matchLabels এর app: এ সেম নাম দিবো । 
    
    - Now, we will define the image:version


## `# 10.2  Apply the changes: `


```bash
kubectl apply -f deployment.yaml 
```
`এখন যদি আমাদের ফাইলটা local এ না থেকে remotely থাকে তাহলে আমাদের তার link provide করতে হবে ।`


**OUTPUT:**

```css
deployment.apps/my-express-demo created
```

`সুবিধা, একটা ফাইলেই সবকিছু manage করতে পারতেছি । যদি scale out করতে মনে চায় তো আমরা, এই ফাইলেই সবকিছু change করে আবার, আপডেট করে দিতে পারবো। same command, "kubectl apply -f deployment.yaml " দিয়ে । `



