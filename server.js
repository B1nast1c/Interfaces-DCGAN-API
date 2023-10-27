const common = require('./common');
const app = require('fastify')({ logger: true });
const PORT = process.env.PORT || common.PORT

const labelsRoutes = require('./routes/labels')
labelsRoutes.forEach(
    (route, _) => {
        app.route(route)
    }
)

app.listen({ port: PORT }, function (err, address) {
    if (err) {
        fastify.log.error(err)
        process.exit(1)
    }
})