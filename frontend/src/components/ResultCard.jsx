function ResultCard({ data }) {
  return (
    <div className="result-card">
      <h2>Prediction Result</h2>

      <p>
        <strong>Predicted Leaf:</strong> {data.prediction}
      </p>

      <p>
        <strong>Confidence:</strong> {data.confidence}%
      </p>

      <p>
        <strong>Leaf Name:</strong> {data.leaf_name}
      </p>

      <hr />

      <h3>Medicinal Uses</h3>

      {data.medical_uses.length === 0 ? (
        <p>No medicinal data available.</p>
      ) : (
        data.medical_uses.map((item, index) => (
          <div key={index} className="medicine-box">
            <p><strong>Disease:</strong> {item.disease}</p>
            <p><strong>Symptoms:</strong> {item.symptoms}</p>
            <p><strong>Remedies:</strong> {item.remedies}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default ResultCard;