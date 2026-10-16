// Attendre que config.js charge et redéfinir les constantes
setTimeout(() => {
    if (window.telegramConfig) {
        window.BOT_TOKEN = window.telegramConfig.BOT_TOKEN;
        window.CHAT_ID = window.telegramConfig.CHAT_ID;
        console.log('Telegram config initialized:', window.BOT_TOKEN ? 'OK' : 'EMPTY');
    }
}, 100);
