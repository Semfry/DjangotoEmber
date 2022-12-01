import Component from '@glimmer/component';
import { tracked } from '@glimmer/tracking';
import { action } from '@ember/object';

export default class AddfavgameComponent extends Component {
  @tracked gdata;
  @tracked ydata;

  @action
  createFavg(event) {
    event.preventDefault();

    if (this.gdata && this.ydata && this.args.onCreate) {
      this.args.onCreate(this.gdata, this.ydata);

      // reset the message input
      this.gdata = '';
      this.ydata = '';
    }
  }
}
