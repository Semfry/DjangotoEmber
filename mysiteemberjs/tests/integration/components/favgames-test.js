import { module, test } from 'qunit';
import { setupRenderingTest } from 'mysiteemberjs/tests/helpers';
import { render } from '@ember/test-helpers';
import { hbs } from 'ember-cli-htmlbars';

module('Integration | Component | favgames', function (hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function (assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`<favgames />`);

    assert.dom(this.element).hasText('');

    // Template block usage:
    await render(hbs`
      <favgames>
      Game Name: Start Year:
      </favgames>
    `);

    assert.dom(this.element).hasText('');
  });
});
