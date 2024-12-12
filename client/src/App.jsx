import { useState } from "react";
import ReadButton from "./componentz/ReadButton";
import ConnectForm from "./componentz/connectForm";
import DiscoverDevices from "./componentz/discoverDevices";
import DeviceList from "./componentz/DeviceList";
import TagList from "./componentz/tagList";
function App() {
  const [deviceList, setDeviceList] = useState(false);
  const [activeDevice, setActiveDevice] = useState(false);
  const [tagList, setTagList] = useState(false);

  return (
    <div className="justify-right h-screen flex">
      <DiscoverDevices setDeviceList={setDeviceList} />
      <div className={"m-4"}>
        {deviceList && (
          <DeviceList
            deviceList={deviceList}
            activeDevice={activeDevice}
            setActiveDevice={setActiveDevice}
          />
        )}
      </div>
      <div className="m-4">
        <TagList
          activeDevice={activeDevice}
          tagList={tagList}
          setTagList={setTagList}
        />
      </div>
    </div>
  );
}

export default App;
