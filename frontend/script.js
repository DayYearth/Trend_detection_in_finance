document.getElementById("uploadForm").addEventListener("submit", async function (event) {
    event.preventDefault(); // Ngăn chặn hành động mặc định của form
  
    const fileInput = document.getElementById("csvFile");
    const modelSelect = document.getElementById("modelSelect");
    const output = document.getElementById("output");
  
    // Kiểm tra nếu chưa có file
    if (!fileInput.files.length) {
      output.textContent = "Please select a CSV file.";
      return;
    }
  
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);
    formData.append("model", modelSelect.value);
  
    try {
      output.textContent = "Processing...";
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData,
      });
  
      if (!response.ok) {
        throw new Error("Error while predicting trends. Please check the backend.");
      }
  
      const result = await response.json();
      if (result.error) {
        output.textContent = `Error: ${result.error}`;
      } else {
        output.textContent = JSON.stringify(result.predictions, null, 2);
      }
    } catch (error) {
      output.textContent = `Error: ${error.message}`;
    }
  });
  