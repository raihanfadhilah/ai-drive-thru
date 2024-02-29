const fs = require('fs');
require('dotenv').config();
const crypto = require('crypto');
const path = require('path');

const envPath = path.resolve(process.cwd(), '.env');

// Function to append environment variable to .env file
const appendToEnvFile = (key, value) => {
    const envVarString = `${key}=${value}`;
    // Check if the key already exists and replace it
    let envContent = fs.existsSync(envPath) ? fs.readFileSync(envPath, 'utf-8') : '';
    const regex = new RegExp(`^${key}=.*`, 'gm');
    if (envContent.match(regex)) {
        envContent = envContent.replace(regex, envVarString);
    } else {
        envContent += envVarString;
    }
    fs.writeFileSync(envPath, envContent, 'utf-8');
};


// Convert variables (You might not need this function if you are directly using environment variables)
const getEnvVar = (variable) => process.env[variable];

// Unique Key generation based on the current date
const uniqueKey = (date) => {
    const nonce = date.toISOString().slice(0, 19) + '.000Z';
    return getEnvVar('BSP_SECRET_KEY') + nonce;
};

// Signable content creation
const signableContent = (method, url, contentType, contentMd5, organization) => {
    const requestPath = url.replace(/^https?:\/\/[^\/]+\//, '/');
    return [method, requestPath, contentType, contentMd5, organization].filter(p => p && p.length > 0).join('\n');
};

// Adjust calculateSignature to return both date and signature
const calculateSignature = () => {
    const date = new Date().toGMTString(); // Store the GMT string format of the date
    const key = uniqueKey(new Date(date));
    const organization = process.env.BSP_ORGANIZATION;
    // Example request details
    const method = 'POST';
    const url = "/order/3/orders/1";
    const contentType = 'application/json';
    const contentMd5 = undefined;

    const sc = signableContent(method, url, contentType, contentMd5, organization);
    const hmac = crypto.createHmac('sha512', key).update(sc).digest('base64');
    return { date, signature: hmac };
};

// Update generateAccessKey to use the modified calculateSignature
const generateAccessKey = () => {
    const { date, signature } = calculateSignature();
    const sharedKey = process.env.BSP_SHARED_KEY;
    const accessKey = `AccessKey ${sharedKey}:${signature}`;
    console.log('Generated BSP Access Key:', accessKey);

    // Append DATE and BSP_ACCESS_KEY to .env file
    appendToEnvFile('DATE', date);
    appendToEnvFile('BSP_ACCESS_KEY', accessKey);
//     return {accessKey, date};
};

generateAccessKey();
