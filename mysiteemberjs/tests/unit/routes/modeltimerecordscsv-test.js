import { module, test } from 'qunit';
import { setupTest } from 'mysiteemberjs/tests/helpers';

module('Unit | Route | modeltimerecordscsv', function (hooks) {
  setupTest(hooks);

  test('it exists', function (assert) {
    let route = this.owner.lookup('route:modeltimerecordscsv');
    assert.ok(route);
  });
});
