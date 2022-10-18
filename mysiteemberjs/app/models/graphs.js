import Model, { attr } from '@ember-data/model';

export default class GraphsModel extends Model {
  @attr graphname;
  @attr graphlink;
}
