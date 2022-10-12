import { module, test } from 'qunit';
import { setupRenderingTest } from 'shaun-site/tests/helpers';
import { render } from '@ember/test-helpers';
import { hbs } from 'ember-cli-htmlbars';

module('Integration | Component | modlists', function (hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function (assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`<modlists />`);

    assert.dom(this.element).hasText('');

    // Template block usage:
    await render(hbs`
      <modlists>
      Mod Name: Release Year: Game Name: Download Link:\"
      </modlists>
    `);

    assert
      .dom(this.element)
      .hasText('Mod Name: Release Year: Game Name: Download Link:"');
  });
});
