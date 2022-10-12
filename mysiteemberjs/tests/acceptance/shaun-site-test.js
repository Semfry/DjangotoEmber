import { module, test } from 'qunit';
import { visit, currentURL } from '@ember/test-helpers';
import { setupApplicationTest } from 'shaun-site/tests/helpers';

module('Acceptance | shaun site', function (hooks) {
  setupApplicationTest(hooks);

  test('visiting /', async function (assert) {
    await visit('/');
    assert.dom('Pageheader').exists;

    assert.strictEqual(currentURL(), '/');
  });
});
