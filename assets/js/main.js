// Simple student-grade copy-to-clipboard code
function copyToClipboard() {
    const linkEl = document.getElementById("short-url-link");
    if (!linkEl) return;
    
    // Get absolute URL from href
    const copyText = linkEl.getAttribute("href");
    
    navigator.clipboard.writeText(copyText).then(() => {
        const btn = document.getElementById("btn-copy");
        if (btn) {
            btn.innerText = "Copied!";
            btn.style.backgroundColor = "#e6f4ea";
            btn.style.color = "#137333";
            btn.style.borderColor = "#82c315"; // simple light green accent
            
            // Reset button after 2 seconds
            setTimeout(() => {
                btn.innerText = "Copy";
                btn.style.backgroundColor = "#ffffff";
                btn.style.color = "#374151";
                btn.style.borderColor = "#d1d5db";
            }, 2000);
        }
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}
