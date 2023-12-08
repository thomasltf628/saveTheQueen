import React from 'react';

const DataTable = ({ jsonData }) => {
  if (!jsonData) {
    return null;
  }

  const tableData = jsonData.map((item, index) => ({
        id: index +1,
        source: item.source,
        price:item.price,
        mileage: item.mileage,
        location: item.location,
        link_to_buyer: item.link_to_buyer,
        year: item.year,
  }
  )
  )

  return (
    <div>
    <table style={{width: '100%', height: '400px', borderWidth: '2px'}}>
      <thead>
        <tr>
          <th>ID</th>
          <th>Source</th>
          <th>Price</th>
          <th>Mileage</th>
          <th>Year</th>
          <th>Location</th>
          <th>Link</th>
        </tr>
      </thead>
      <tbody>
        {tableData.map((rowData) => (
          <tr key={rowData.id}>
            <td>{rowData.id}</td>
            <td>{rowData.source}</td>
            <td>{rowData.price}</td>
            <td>{rowData.mileage}</td>
            <td>{rowData.year}</td>
            <td>{rowData.location}</td>
            <td><a href={rowData.link_to_buyer}>Click to contact seller</a></td>
          </tr>
        ))}
      </tbody>
    </table>
    </div>
  );
};

export default DataTable;
