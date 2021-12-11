'use strict';

const fs = require('fs');

let data = fs.readFileSync('C:/Users/Oğuz KABA/dosya.txt', 'utf-8');

console.log(data);

console.log('Dosya okundu');