import Component from '@glimmer/component';
import { tracked } from '@glimmer/tracking';
import { action } from '@ember/object';

export default class FavgamesComponent extends Component {

    @action
    addFavg(ngamename, nstartyear) {
      this.model = [...this.model, {
        gamename: {ngamename},
        startyear: {nstartyear}
      }];
    }
}

