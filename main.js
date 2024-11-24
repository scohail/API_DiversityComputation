// Import necessary modules
const { app, BrowserWindow, dialog } = require('electron');
const path = require('node:path');
const axios = require('axios');
const fs = require('fs');

// Function to create the main application window
function createWindow() {
  // Create the browser window
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
    },
  });

  // Load the HTML file
  mainWindow
    .loadFile('index.html')
    .then(() => {
      // Example: Interaction with Flask API
      testFlaskAPI();
    })
    .catch((error) => {
      console.error('Error loading HTML file:', error.message);
    });

  // Optionally open Developer Tools
  mainWindow.webContents.openDevTools();
}

async function uploadFile() {
  const fileInput = document.getElementById('fileInput');
  const resultsDiv = document.getElementById('results');

  if (!fileInput.files.length) {
    alert('Please select a file.');
    return;
  }

  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  try {
    // Step 1: Upload the file
    const uploadResponse = await fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      body: formData,
    });

    if (!uploadResponse.ok) {
      const errorData = await uploadResponse.json();
      resultsDiv.innerHTML = `<p style="color: red;">Error: ${errorData.error}</p>`;
      return;
    }

    const uploadData = await uploadResponse.json();
    const columns = uploadData.columns;
    const filePath = uploadData.file_path;

    console.log('Columns:', columns);
    console.log('Uploaded file path:', filePath);

    // Step 2: Calculate the metric
    const calculateResponse = await fetch('http://127.0.0.1:5000/calculate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        file_path: filePath, // Replace this with actual uploaded file path
        columns: columns, // Select first two columns
        metric: 'correlation_coefficient',
      }),
    });

    if (!calculateResponse.ok) {
      const errorData = await calculateResponse.json();
      resultsDiv.innerHTML = `<p style="color: red;">Error: ${errorData.error}</p>`;
      return;
    }

    const calculateData = await calculateResponse.json();
    resultsDiv.innerHTML = `
      <h3>Results:</h3>
      <ul>
        ${Object.entries(calculateData).map(([key, value]) => `<li>${key}: ${value}</li>`).join('')}
      </ul>
    `;
  } catch (error) {
    resultsDiv.innerHTML = `<p style="color: red;">An error occurred: ${error.message}</p>`;
  }
}

// Called when Electron has finished initialization
app.whenReady().then(() => {
  createWindow();

  // Recreate a window in macOS when the dock icon is clicked
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

// Quit the application when all windows are closed
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
