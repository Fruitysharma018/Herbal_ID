import { useState, useEffect } from "react";
import UploadBox from "./components/UploadBox";
import ResultCard from "./components/ResultCard";
import Login from "./pages/Login";
import Signup from "./pages/Signup";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [showSignup, setShowSignup] = useState(false);
  const [result, setResult] = useState(null);

  // Check login status on page reload
  useEffect(() => {
    const loggedIn = localStorage.getItem("isLoggedIn");
    if (loggedIn === "true") {
      setIsLoggedIn(true);
    }
  }, []);

  // Called after successful login
  const handleLogin = (userId) => {
    localStorage.setItem("isLoggedIn", "true");
    localStorage.setItem("user_id", userId); // important for backend
    setIsLoggedIn(true);
  };

  // Logout user
  const handleLogout = () => {
    localStorage.removeItem("isLoggedIn");
    localStorage.removeItem("user_id");
    setIsLoggedIn(false);
    setResult(null);
  };

  // ------------------ AUTH SCREENS ------------------
  if (!isLoggedIn) {
    return (
      <div className="page">
        <div className="container">
          {showSignup ? (
            <Signup onSwitchToLogin={() => setShowSignup(false)} />
          ) : (
            <Login
              onLogin={handleLogin}
              onSwitchToSignup={() => setShowSignup(true)}
            />
          )}
        </div>
      </div>
    );
  }

  // ------------------ MAIN APP ------------------
  return (
    <div className="page">
      <div className="container">
        <button
          onClick={handleLogout}
          style={{
            float: "right",
            background: "#c62828",
            marginBottom: "10px",
          }}
        >
          Logout
        </button>

        <h1>🌿 Herbal ID</h1>
        <p className="subtitle">
          Upload a leaf image to identify plant health and disease
        </p>

        <UploadBox onResult={setResult} />

        {result && <ResultCard data={result} />}
      </div>
    </div>
  );
}

export default App;
