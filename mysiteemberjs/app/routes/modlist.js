import Route from '@ember/routing/route';

import { service } from '@ember/service';

import RSVP from 'rsvp';

export default class ModlistRoute extends Route {
  @service store;

  async model() {
    return RSVP.hash({
      modlists: this.store.findAll('modlist'),
    });
  }
}
