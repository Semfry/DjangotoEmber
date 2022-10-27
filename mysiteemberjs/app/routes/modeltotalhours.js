import Route from '@ember/routing/route';

import { service } from '@ember/service';

import RSVP from 'rsvp';

export default class modeltotalhoursRoute extends Route {
@service store;

  async model() {
    return RSVP.hash({
      modeltotalhours: this.store.findAll('modeltotalhours'),
    });
  }
}

