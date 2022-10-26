import Route from '@ember/routing/route';

import { service } from '@ember/service';

import RSVP from 'rsvp';

export default class modeltimerecordscsvsRoute extends Route {
@service store;

  async model() {
    return RSVP.hash({
      modeltimerecordscsvs: this.store.findAll('modeltimerecordscsvs'),
    });
  }
}
