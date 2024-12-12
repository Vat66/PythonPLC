function DeviceCard({ device, activeDevice, setActiveDevice }) {

  const setActiveDeviceHandler = () => {
    setActiveDevice(device)
  };

  const resetActiveDeviceHandler = () => {
    setActiveDevice(false)
  };


  return (
    <>
      {device && (
        <div>
          <button
            className="btn m-2"
            onClick={() => document.getElementById("my_modal_5").showModal()}
          >
            <p>{device.ProductName}</p>
            <p>{device.Vendor}</p>
          </button>
          <dialog
            id="my_modal_5"
            className="modal modal-bottom sm:modal-middle"
          >
            <div className="modal-box">
              <h3 className="font-bold text-lg">{device.ProductName}</h3>
              <h3 className="font-bold text-lg">{device.Vendor}</h3>
              <h3 className="font-bold text-lg">{device.IPAddress}</h3>
              <div className="pt-4">
                <p className="text-sm">Device Id: {device.DeviceID}</p>
                <p className="text-sm">Product Code: {device.ProductCode}</p>
                <p className="text-sm">Revision: {device.Revision}</p>
                <p className="text-sm">Serial Number: {device.SerialNumber}</p>
              </div>
              <div className="modal-action">
                <form method="dialog">
                  {/* if there is a button in form, it will close the modal */}
                  <button class="btn btn-secondary" onClick={resetActiveDeviceHandler}>Reset</button>
                  <button className="btn btn-success" onClick={setActiveDeviceHandler}>Set as Active</button>
                  <button className="btn">Close</button>
                </form>
              </div>
            </div>
          </dialog>
        </div>
      )}
    </>
  );
}

export default DeviceCard;
