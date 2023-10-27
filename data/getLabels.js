const fs = require('fs');
const csv = require('csv-parser');

function getTopics(filename, column) {
    return new Promise((resolve, reject) => {
        const results = [];

        fs.createReadStream(filename)
            .pipe(csv())
            .on('data', (data) => {
                const label = data[column];
                results.push(label);
            })
            .on('end', () => {
                resolve(results);
            })
            .on('error', (error) => {
                reject(error);
            });
    });
}

module.exports = getTopics;
