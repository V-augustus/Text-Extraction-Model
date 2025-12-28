// server.js
const express = require('express');
const multer = require('multer');
const vision = require('@google-cloud/vision');
const xlsx = require('xlsx');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Enable CORS for frontend communication
app.use(cors());
// Serve static files (our frontend HTML/JS) from a 'public' folder
app.use(express.static('public'));
app.use(express.json());

// --- CONFIGURATION ---

// Configure Multer for temporary file storage
const upload = multer({ dest: 'uploads/' });

// Configure Google Cloud Vision Client
// Ensure 'google-key.json' is in the same directory as server.js
const client = new vision.ImageAnnotatorClient({
    keyFilename: './google-key.json'
});


// --- ROUTES ---

// The main route to handle image upload and processing
app.post('/process-image', upload.single('transactionImage'), async (req, res) => {
    if (!req.file) {
        return res.status(400).send('No image uploaded.');
    }

    const filePath = req.file.path;

    try {
        console.log(`Processing file: ${filePath}...`);

        // 1. Send image to Google Cloud Vision API for Text Detection
        // documentTextDetection works better for dense text like receipts than plain textDetection
        const [result] = await client.documentTextDetection(filePath);
        const fullTextAnnotation = result.fullTextAnnotation;

        // Basic error check if no text found
        if (!fullTextAnnotation || !fullTextAnnotation.text) {
             fs.unlinkSync(filePath); // Clean up upload
             return res.json({ success: true, rawText: "No text detected in image." });
        }
        
        const extractedText = fullTextAnnotation.text;
        console.log("Text extracted successfully.");


        // 2. Generate Output Files (We will generate them temporarily)
        const timestamp = Date.now();
        const outputDir = path.join(__dirname, 'public/downloads');
        
        // Ensure download directory exists
        if (!fs.existsSync(outputDir)){
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // --- Generate TXT File ---
        const txtFilename = `transaction_${timestamp}.txt`;
        const txtPath = path.join(outputDir, txtFilename);
        fs.writeFileSync(txtPath, extractedText);


        // --- Generate Excel File ---
        // Splitting text by new lines to create rows in Excel
        const lines = extractedText.split('\n').map(line => [line]);
        
        const wb = xlsx.utils.book_new();
        // Create a worksheet with headers
        const wsData = [["Extracted Transaction Data"], ...lines];
        const ws = xlsx.utils.aoa_to_sheet(wsData);
        xlsx.utils.book_append_sheet(wb, ws, "Transaction");
        
        const xlsxFilename = `transaction_${timestamp}.xlsx`;
        const xlsxPath = path.join(outputDir, xlsxFilename);
        xlsx.writeFile(wb, xlsxPath);

        // 3. Cleanup uploaded image file
        fs.unlinkSync(filePath);

        // 4. Send response back to frontend with download links
        res.json({
            success: true,
            rawText: extractedText,
            txtDownloadLink: `/downloads/${txtFilename}`,
            xlsxDownloadLink: `/downloads/${xlsxFilename}`
        });


    } catch (error) {
        console.error('Error processing image:', error);
        // Try to clean up file if it exists
        if (fs.existsSync(filePath)) fs.unlinkSync(filePath);
        res.status(500).send('Error during OCR processing.');
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
    // Create uploads folder automatically
    if (!fs.existsSync('./uploads')){
        fs.mkdirSync('./uploads');
    }
});
