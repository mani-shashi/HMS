import React from "react";

const Loading = () => {
  return (
    <div className="relative">
      <div className="outer_container absolute left-[-40px]">
        <div className="lds-ellipsis">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
        </div>
      </div>
    </div>
  );
};

export default Loading;
