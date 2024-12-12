import { useEffect } from "react";
import TagCard from "./tagCard";

function TagList({ activeDevice, tagList, setTagList }) {
  useEffect(() => {
    getTags(activeDevice.IPAddress);
  }, [activeDevice]);

  const getTags = async (ip_address) => {
    try {
      const responce = await fetch("http://127.0.0.1:5000/tags", {
        method: "POST",
        headers: {
          "Content-Type": "application/json", // Specify JSON content
        },
        body: JSON.stringify({
          ip_address: ip_address,
        }),
      });
      const data = await responce.json();
      console.log(data);
      await setTagList(data);
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <>
      {activeDevice && (
        <div>
          <div>
            <h3 className="font-bold text-lg">{activeDevice.ProductName}</h3>
            <h3 className="font-bold text-lg">{activeDevice.Vendor}</h3>
            <h3 className="font-bold text-lg">{activeDevice.IPAddress}</h3>
          </div>
          <div>
            {tagList[0] && (
              <div className="overflow-x-auto">
                <table className="table table-xs table-pin-rows table-pin-cols">
                  <thead>
                    <tr>
                      <th></th>
                      <td>Tag Name</td>
                      <td>DataType</td>
                      <td>Scope 0</td>
                      <td>Scope 1</td>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    {tagList.map((tag, index) => (
                      <TagCard
                        tag={tag}
                        key={index}
                        index={index}
                        activeDevice={activeDevice}
                      />
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      )}
    </>
  );
}
export default TagList;
