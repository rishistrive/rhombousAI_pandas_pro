import React, { useState } from 'react';
import axios from 'axios';
import FileUploader from './components/FileUploader';
import ProcessedData from './components/ProcessedData';

const App = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [processedData, setProcessedData] = useState(null);

  const handleFileChange = (file) => {
    setSelectedFile(file);
  };

  const handleFileUpload = async () => {
    try {
      const formData = new FormData();
      formData.append('file', selectedFile);

      // Send file to the backend for processing
      const response = await axios.post('http://localhost:8000/api/process-data/', formData);


      // Set the processed data in state
      setProcessedData(response.data);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div>
      <h1>Data Processing Web App</h1>

      <FileUploader onFileChange={handleFileChange} onFileUpload={handleFileUpload} />

      {processedData && <ProcessedData data={processedData} />}
    </div>
  );
};

export default App;
