import React, { useState } from 'react';

const FileUpload = ({ onFileUpload }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedFile(file);

    if (file) {
        const formData = new FormData();
        formData.append('file', file);
        onFileUpload(formData); // Use onFileUpload, not onFileSelect
      }    
  };

  return (
    <div>
      <input
        type="file"
        accept=".jpg, .jpeg, .png, .gif, .pdf"  // Specify the file types you want to allow
        onChange={handleFileChange}
      />
      {selectedFile && <p>Selected File: {selectedFile.name}</p>}
    </div>
  );
};

export default FileUpload;