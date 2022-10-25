import Route from '@ember/routing/route';

import { service } from '@ember/service';

import RSVP from 'rsvp';

export default class ModeltimerecordscsvRoute extends Route {
@service store;

  async model() {
    return RSVP.hash({
      modeltimerecordscsv: this.store.findAll('modeltimerecordscsv'),
    });
  }
}
