// contentScript.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'GET_YOUTUBE_URL') {
      const videoUrl = window.location.href; // Get the current URL
      sendResponse({ url: videoUrl });
  }
});
