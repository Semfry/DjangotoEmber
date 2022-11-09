import Route from '@ember/routing/route';

import { service } from '@ember/service';

import RSVP from 'rsvp';

export default class GraphsRoute extends Route {
  @service store;

  model() {
    return this.store.findAll("graphs");
  }
}
