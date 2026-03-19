import { useState } from "react";

function Signup({ onSwitchToLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = (e) => {
    e.preventDefault();

    if (!email || !password) {
      alert("Please fill all fields");
      return;
    }

    // Get existing users
    const users = JSON.parse(localStorage.getItem("users")) || [];

    // Check if user already exists
    const userExists = users.find((u) => u.email === email);
    if (userExists) {
      alert("User already exists ❌");
      return;
    }

    // Save new user
    users.push({ email, password });
    localStorage.setItem("users", JSON.stringify(users));

    alert("Signup successful ✅");
    onSwitchToLogin();
  };

  return (
    <div className="login-container">
      <h2>🌿 Create Account</h2>

      <form onSubmit={handleSignup}>
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

        <button type="submit">Sign Up</button>
      </form>

      <p style={{ marginTop: "10px" }}>
        Already have an account?{" "}
        <span
          style={{ color: "green", cursor: "pointer" }}
          onClick={onSwitchToLogin}
        >
          Login
        </span>
      </p>
    </div>
  );
}

export default Signup;