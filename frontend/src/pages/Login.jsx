import { useState } from "react";

function Login({ onLogin, onSwitchToSignup }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();

    const users = JSON.parse(localStorage.getItem("users")) || [];

    const validUser = users.find(
      (u) => u.email === email && u.password === password
    );

    if (validUser) {
      onLogin();
    } else {
      alert("Invalid credentials ❌");
    }
  };

  return (
    <div className="login-container">
      <h2>🌿 Leaf System Login</h2>

      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit">Login</button>
      </form>

      <p style={{ marginTop: "10px" }}>
        New user?{" "}
        <span
          style={{ color: "green", cursor: "pointer" }}
          onClick={onSwitchToSignup}
        >
          Create account
        </span>
      </p>
    </div>
  );
}

export default Login;