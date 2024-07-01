const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

app.post('/draft-email', (req, res) => {
    const { bank, clients, tone } = req.body;
    const emailContent = `Drafting email for bank: ${bank} with tone: ${tone}`;
    res.json({ emailDraft: emailContent, status: "success" });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
