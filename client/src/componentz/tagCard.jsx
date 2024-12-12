import { useState } from "react";

function TagCard({ tag, index, activeDevice }) {
    const [boolStatus, setBoolStatus] = useState("Nothing")

  const writeBool = async (ip_address) => {
    try {
      const responce = await fetch("http://127.0.0.1:5000/writeBool", {
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
    } catch (error) {
      console.log(error);
    }
  };

  const readBool = async (tag_name, ip_address) => {
    try {
      const responce = await fetch("http://127.0.0.1:5000/readBool", {
        method: "POST",
        headers: {
          "Content-Type": "application/json", // Specify JSON content
        },
        body: JSON.stringify({
          tag_name: tag_name,
          ip_address: ip_address,
        }),
      });
      const data = await responce.json();
      console.log(data);
      setBoolStatus(data)
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <>
      {tag && (
        <>
          <tr>
            <button
              className="btn btn-info btn-sm"
              onClick={() => {
                document.getElementById(`my_modal_${tag.TagName}`).showModal();
                setBoolStatus("Nothing")
                console.log(tag);
              }}
            >
              View Tag
            </button>
            <th>{index}</th>
            <td>{tag.TagName}</td>
            <td>{tag.DataType}</td>
            <td>{tag.Scope0}</td>
            <td>{tag.Scope1}</td>
            <th>{index}</th>
          </tr>
          <dialog
            id={`my_modal_${tag.TagName}`}
            className="modal modal-bottom sm:modal-middle"
          >
            <div className="modal-box">
              <h3 className="font-bold text-lg">{tag.TagName}</h3>
              <p className="py-4">
                <td>{tag.DataType}</td>
                {boolStatus === true && <div className="badge badge-primary">TRUE</div>}
                {boolStatus === false && <div className="badge badge-secondary">FALSE</div>}
              </p>
              <div className="modal-action">
                <button
                  className="btn btn-primary"
                  onClick={() => {
                    readBool(tag.TagName, activeDevice.IPAddress);
                  }}
                >
                  Read Bool
                </button>
                <button
                  className="btn btn-outline btn-accent"
                  onClick={() => {
                    writeBool(tag.TagName, 1, activeDevice.IPAddress);
                  }}
                >
                  Write Bool 1
                </button>
                <button
                  className="btn btn-outline btn-accent"
                  onClick={() => {
                    writeBool(tag.TagName, 0, activeDevice.IPAddress);
                  }}
                >
                  Write Bool 0
                </button>
                <form method="dialog">
                  {/* if there is a button in form, it will close the modal */}
                  <button className="btn">Close</button>
                </form>
              </div>
            </div>
          </dialog>
        </>
      )}
    </>
  );
}
export default TagCard;
