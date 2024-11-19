const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello, Dockerized World!');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`App listening on port ${PORT}`));