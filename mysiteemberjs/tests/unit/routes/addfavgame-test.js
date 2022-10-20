import { module, test } from 'qunit';
import { setupTest } from 'mysiteemberjs/tests/helpers';

module('Unit | Route | addfavgame', function (hooks) {
  setupTest(hooks);

  test('it exists', function (assert) {
    let route = this.owner.lookup('route:addfavgame');
    assert.ok(route);
  });
});
