chrome.runtime.onInstalled.addListener(() => {
  console.log("YouTube Downloader Extension Installed");
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'DOWNLOAD_VIDEO') {
    // Start your download logic here
    fetch(`http://localhost:5000/download?url=${encodeURIComponent(request.url)}`)
      .then(response => response.json())
      .then(result => {
        // Store download message in local storage
        chrome.storage.local.set({ downloadMessage: result.message });
        sendResponse({ success: true });
      })
      .catch(error => {
        console.error('Error in background download:', error);
        sendResponse({ success: false, error: error.message });
      });
    return true; // Indicate that you will send a response asynchronously
  }
});
