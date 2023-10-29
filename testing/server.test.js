const tap = require("tap");
const app = require("../app");
const { getLabels } = require("../controllers/labels");
const common = require("../common");

tap.test("GET `/` route", async (t) => {
  var response = await getLabels();

  t.plan(4);
  t.teardown(() => app.close());

  app.inject(
    {
      method: "GET",
      url: "/api/labels",
    },
    (err, res) => {
      t.error(err);
      t.equal(res.statusCode, 200);
      t.equal(res.headers["content-type"], "application/json; charset=utf-8");
      t.same(JSON.parse(res.payload), response);
    }
  );
});
