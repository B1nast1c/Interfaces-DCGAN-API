const {
    getLabels
} = require('../controllers/labels')

const routes = [{
    method: 'GET',
    url: '/api/labels',
    handler: getLabels
}]

module.exports = routes