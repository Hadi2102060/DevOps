
<br>

---

<br>

# `#9. Scale app in Kubernetes: `

<br>

---

<br>

`আগের পার্টে আমরা যখন, Kubernetes এ থাকা কোন server কোন কারণে বন্ধ হয়েছিল তখন,  Kubernetes একা একা সেই server restart করে দিয়েছিলো । এর জন্য কিছুক্ষন আমাদের server টা বন্ধ ছিলো । কিন্তু, আমরা চাচ্ছি না যে, আমাদের server টা একটু সময়ের জন্যও বন্ধ হোক । এর জন্য আমরা, আমাদের application এর multiple instance তৈরি করতে পারি । এতে আমরা দুইটা সুবিধা পাবো,   `

i) যদি  সার্ভার কোন কারণে বন্ধ হয়ে যায় তাহলে অন্য instance এ সার্ভারটা চালু থাকবে । 
ii) যদি আমাদের application এ traffic অনেক বেশি হয়, সেটাও, maintain করা যাবে । 

**For creating 4 instance:**
```bash
kubectl scale deployment express-demo --replicas=4
```

**See the effect:**
```bash
kubectl get pods                                  
```

**OUTPUT:**
```css
NAME                            READY   STATUS    RESTARTS        AGE
express-demo-77b85977d4-6k5cz   1/1     Running   0               86s
express-demo-77b85977d4-6q7cm   1/1     Running   0               86s
express-demo-77b85977d4-r4wqn   1/1     Running   4 (4m3s ago)    4h
express-demo-77b85977d4-rz5dq   1/1     Running   0               86s
my-web-app-77879848cb-xmz6g     1/1     Running   2 (3h49m ago)   13h
```


IN `RESTARTS` section, we can see how many times a pod restart.


