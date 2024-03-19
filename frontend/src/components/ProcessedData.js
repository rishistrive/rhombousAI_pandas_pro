import React from 'react';

const ProcessedData = ({ data }) => {
  return (
    <div style={{margin: "100px"}}>
      <h2>Processed Data</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            {Object.keys(data[0]).map((key, index) => (
              <th key={index}>{key}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              {Object.values(item).map((value, index) => (
                <td key={index}>{value}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProcessedData;
