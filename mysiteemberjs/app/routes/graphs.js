import Route from '@ember/routing/route';

import { service } from '@ember/service';

import RSVP from 'rsvp';

export default class GraphsRoute extends Route {
@service store;

  async model() {
    return RSVP.hash({
      graphs: this.store.findAll('graphs'),
    });
  }
}
