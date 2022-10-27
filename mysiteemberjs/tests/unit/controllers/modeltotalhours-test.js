import { module, test } from 'qunit';
import { setupTest } from 'mysiteemberjs/tests/helpers';

module('Unit | Controller | modeltotalhours', function (hooks) {
  setupTest(hooks);

  // TODO: Replace this with your real tests.
  test('it exists', function (assert) {
    let controller = this.owner.lookup('controller:modeltotalhours');
    assert.ok(controller);
  });
});
