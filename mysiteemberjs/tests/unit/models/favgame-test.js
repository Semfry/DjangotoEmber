import { module, test } from 'qunit';
import { setupTest } from 'shaun-site/tests/helpers';

module('Unit | Model | favgame', function (hooks) {
  setupTest(hooks);

  // Replace this with your real tests.
  test('it exists', function (assert) {
    let store = this.owner.lookup('service:store');
    let model = store.createRecord('favgame', {});
    assert.ok(model);
  });
});
