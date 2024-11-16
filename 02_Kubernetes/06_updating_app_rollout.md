
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

```bash
docker build -t yourusername/node-api:latest .
```



