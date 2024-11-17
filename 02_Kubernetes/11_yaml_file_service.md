<br>

---
<br>

# `#10: YAML Configuration:) for service api: `

<br>
<br>

---
---

`আমরা আগের বারে মতো, kubernetes এর ওয়েবসাইট থেকে  থেকে nginx এর জন্য, service এর  যে yaml file আছে সেইটা কপি করবো ।` 

```yml
kind: Service
apiVersion: v1
metadata:
  # Unique key of the Service instance
  name: service-my-express-demo
spec:
  ports:
    # Accept traffic sent to port 80
    - name: http
      port: 8080
      targetPort: 3000
  selector:
    # Loadbalance traffic across Pods matching
    # this label selector
    app: express
  # Create an HA proxy in the cloud provider
  # with an External IP address - *Only supported
  # by some cloud providers*
  type: LoadBalancer

```
 template:
    metadata:
      labels:
        # Apply this label to pods and default
        # the Deployment label selector to this value
        app: express

`এখানে, আমরা খেয়াল করবো যে, আমদের deployment.yml ফাইলে,template এরপর metadata এরপর  labels এ app এর যেই নামটা দেওয়া থাকে আমরা সেই নামটা দিব । `


### **`apply the command below:`**

`Same command but file name different: `
```bash
kubectl apply -f service.yml  
```

### **`Delete a services: `**

```bash
kubectl delete -f service.yml
```
