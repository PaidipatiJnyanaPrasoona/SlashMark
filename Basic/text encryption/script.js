// script.js

const inputText = document.getElementById('input-text');
const encryptBtn = document.getElementById('encrypt-btn');
const decryptBtn = document.getElementById('decrypt-btn');
const outputText = document.getElementById('output-text');

// Generate a random key for encryption and decryption
const key = CryptoJS.lib.WordArray.random(16);

encryptBtn.addEventListener('click', () => {
    const text = inputText.value;
    const encryptedText = CryptoJS.AES.encrypt(text, key).toString();
    outputText.value = encryptedText;
});

decryptBtn.addEventListener('click', () => {
    const encryptedText = inputText.value;
    const decryptedText = CryptoJS.AES.decrypt(encryptedText, key).toString(CryptoJS.enc.Utf8);
    outputText.value = decryptedText;
});