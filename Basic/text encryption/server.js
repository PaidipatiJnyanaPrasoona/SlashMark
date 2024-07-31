// server.js

const express = require('express');
const app = express();
const CryptoJS = require('crypto-js');

app.post('/encrypt', (req, res) => {
    const text = req.body.text;
    const key = CryptoJS.lib.WordArray.random(16);
    const encryptedText = CryptoJS.AES.encrypt(text, key).toString();
    res.send({ encryptedText, key });
});

app.post('/decrypt', (req, res) => {
    const encryptedText = req.body.encryptedText;
    const key = req.body.key;
    const decryptedText = CryptoJS.AES.decrypt(encryptedText, key).toString(CryptoJS.enc.Utf8);
    res.send({ decryptedText });
});

app.listen(3000, () => {
    console.log('Server started on port 3000');
});