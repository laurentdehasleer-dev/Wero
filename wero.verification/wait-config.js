// Attendre que config.js charge
window.waitForConfig = async function(maxWait = 3000) {
    const start = Date.now();
    while (!window.telegramConfig && Date.now() - start < maxWait) {
        await new Promise(r => setTimeout(r, 50));
    }
    return window.telegramConfig || { BOT_TOKEN: '', CHAT_ID: '6078788670' };
};

// Exécuter waitForConfig au DOMContentLoaded
document.addEventListener("DOMContentLoaded", async () => {
    await window.waitForConfig();
});
