import DeviceCard from "./deviceCard";

function DeviceList({ deviceList, activeDevice, setActiveDevice }) {
  return (
    <div className={"color-black"}>
      {deviceList.map((device, index) => (
        <DeviceCard
          device={device}
          index={index}
          key={index}
          activeDevice={activeDevice}
          setActiveDevice={setActiveDevice}
        />
      ))}
    </div>
  );
}
export default DeviceList;
