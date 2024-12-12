function DiscoverDevices({ setDeviceList }) {
  const discoverDevicesHandler = async () => {
    try {
      const responce = await fetch("http://127.0.0.1:5000/discover", {
        method: "POST",
        headers: {
          "Content-Type": "application/json", // Specify JSON content
        },
      });
      const data = await responce.json();
      console.log(data);
      setDeviceList(data)
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <button
      className="btn btn-primary btn-lg m-4"
      onClick={discoverDevicesHandler}
    >
      Discover Devices
    </button>
  );
}

export default DiscoverDevices;
