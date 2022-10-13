import Route from '@ember/routing/route';

import { service } from '@ember/service';

import RSVP from 'rsvp';

export default class FavgameRoute extends Route {
  @service store;

  async model() {
    return RSVP.hash({
      modslists: this.store.findAll('modslists'),
    });
  }
}
