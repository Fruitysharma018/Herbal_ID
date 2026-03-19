import { useState } from "react";

function UploadBox({ onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    if (!file) {
      setError("Please select an image");
      return;
    }

    setError("");
    setLoading(true);

    const formData = new FormData();
    formData.append("image", file);
    formData.append("user_id", localStorage.getItem("user_id"));

    try {
      const res = await fetch("http://127.0.0.1:5000/identify", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      onResult(data);
    } catch (err) {
      setError("Failed to connect to backend");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-box">
      <input
        type="file"
        accept="image/*"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Processing..." : "Identify Leaf"}
      </button>

      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default UploadBox;