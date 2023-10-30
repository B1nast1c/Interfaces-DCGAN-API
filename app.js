const common = require('./common');
const app = require('fastify')({logger: true});
const PORT = process.env.PORT || common.PORT;
const cors = require('@fastify/cors');

const labelsRoutes = require('./routes/labels');
labelsRoutes.forEach((route, _) => {
  app.route(route);
});

app.register(cors, {
  origin: true,
});

app.listen({port: PORT}, function(err) {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});

module.exports = app;
