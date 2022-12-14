import Component from '@glimmer/component';
import { service } from '@ember/service';

export default class GraphsComponent extends Component {
  @service store;

  data = {
    labels: [this.store.peekrecord(user)],
    datasets: [
      {
        label: 'Dataset 1',
        data: [12, 19, 3, 5, 2, 3],
      }
    ]
  };
}
