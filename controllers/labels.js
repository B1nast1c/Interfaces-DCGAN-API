const getTopics = require('../data/getLabels.js')
const common = require('../common');

const getLabels = async (req, res) => {
    labels = getTopics(common.FILE_LOCATION, 'topic')
        .then(
            (data) => {
                data = [...new Set(data)]
                return data
            }
        )
        .catch((err) => {
            console.log(err)
        })

    return labels
}

module.exports = {
    getLabels
}