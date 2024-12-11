import { useState, useRef } from "react";

function ConnectForm() {
  const ipRef = useRef();

  
  const ConnectPLC = async () => {
    const ipAddress = ipRef.current.value;

    try {
      const response = await fetch("http://127.0.0.1:5000/connect", {
        method: "POST",
        headers: {
          "Content-Type": "application/json", // Specify JSON content
        },
        body: JSON.stringify({ ipAddress }), // Send the IP address in the request body
      });

      const data = await response.json(); // Parse the JSON response
      console.log(data);
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred while connecting to the PLC.");
    }
  };

  return (
    <>
      <label className="form-control w-full max-w-xs">
        <div className="label">
          <span className="label-text">What is your name?</span>
          <span className="label-text-alt">Top Right label</span>
        </div>
        <input
          ref={ipRef}
          type="text"
          placeholder="IP address"
          className="input input-bordered w-full max-w-xs"
        />
        <div className="label">
          <span className="label-text-alt">Bottom Left label</span>
          <span className="label-text-alt">Bottom Right label</span>
        </div>
        <button className="btn btn-outline btn-primary" onClick={ConnectPLC}>
          Submit
        </button>
      </label>
    </>
  );
}

export default ConnectForm;
