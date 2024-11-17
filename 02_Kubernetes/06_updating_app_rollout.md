
<br>

---
---

<br>

# `#6 Updating app or Rollout:> `

`-> how to set new version: While updating our app. `

<br>

---
---


In our api, `"testapp/src/App.js"` 

```javascript
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
         My first node js for kubernetes
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
```

**change the line in <p> tag: version02**

```javascript
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
         My first node js for kubernetes:version02
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
```

`এখন আমরা তো আমদের api এ পরিবর্তন করলাম । এখানে, একটা লাইন change করেছি, কিন্তু বাস্তবে তো এই পরিবর্তন টা অনেক বেশি হবে । এখন, এইটা পরিবর্তনটাকে new version দিয়ে আমরা update করবো । অর্থাৎ, আমাদেরকে আবার, নতুন করে docker image তৈরি করতে হবে । কিন্তু আমারা একই repo তে শুধু version টা change করে upload করে দেব ।  `

### `**6.1 build new docker image:**`

`yasin005/node-api` we will find this in docker repo.  

```bash
docker build -t yasin005/node-api:latest .
```

### `**6.2 push the new docker image into the docker repo:**`
```bash
docker push yasin005/nginx:02 
```

`এখন,আমাদের যে website আছে .0.1 version এর সেইটা তো সার্ভারে রানিং । এখন, আমরা তো আমাদের website এর .0.2 version বের করেছি । আমরা চাচ্ছি কোন প্রকার server down করা ছাড়া আমরা আমাদের website কে update করবো । এইটা kubernates খুব ভালো করে handle করতে পারে । আগের বার আমরা, "kubectl create deployment my-nginx --image=nginx:latest" command দিয়ে নতুন একটা deployment তৈরি করেছিলাম । কিন্তু, এইবার আমরা নতুন কোন deployment বানাবো না । আগের টাতেই update করে দিবো ।  `

```bash
 kubectl set image deployment my-web-app nginx=yasin005/nginx:02     
```
`Command breakdown:. kubectl set image deployment (deployment_name) (container_name)=docker_image_repo:version`
`minikube dashbard থেকে pod এ যাবো এর মধ্যে আমরা (container_name) দেখতে পাবো । `
**OUPUT:**
```css
deployment.apps/my-web-app image updated
```

### `6.3 see the effect:) `

```bash 
kubectl get pods 
```

```css                                            
NAME                          READY   STATUS    RESTARTS   AGE
my-web-app-77879848cb-xmz6g   1/1     Running   0          6m46s
```

`অর্থাৎ, আমার আগে যে pod running ছিল যেই image version:0.01 এর উপর সেইটা change হয়ে গেছে version:0.02 । আমরা আগের মতো, minikube dashbard থেকে pod এর মধ্যে যাবো, সেখানে দেখতে পাবো আমাদের image version change হয়ে গেছে । পাশাপাশি আমরা, server চালু করে check করতে পারি । `

```bash 
 minikube service my-web-app
```




