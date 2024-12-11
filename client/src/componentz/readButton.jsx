
function ReadButton() {
  const connectPLC = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/connect", {
        method: "POST",
      });
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const ReadFromPLC = () => {
    connectPLC();
  };

  return (
    <>
      <button onClick={ReadFromPLC()}>Connect</button>
    </>
  );
}

export default ReadButton;
