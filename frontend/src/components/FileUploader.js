import React, { useState } from 'react';

const FileUploader = ({ onFileChange, onFileUpload }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [fileError, setFileError] = useState('');

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    onFileChange(file);

    if (file) {
      const allowedExtensions = ['.csv', '.xls', '.xlsx']; // Allowed file extensions
      const extension = '.' + file.name.split('.').pop();
      if (!allowedExtensions.includes(extension.toLowerCase())) {
        setFileError('Please upload a CSV or Excel file');
      } else {
        setFileError('');
      }
    }
  };

  const handleFileUpload = () => {
    if (selectedFile && !fileError) {
      onFileUpload(selectedFile);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleFileUpload} disabled={!selectedFile || fileError}>
        Upload and Process
      </button>
      {fileError && <div style={{ color: 'red' }}>{fileError}</div>}
    </div>
  );
};

export default FileUploader;
