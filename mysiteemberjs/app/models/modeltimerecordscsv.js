import Model, { attr } from '@ember-data/model';

export default class GraphsModel extends Model {
  @attr date;
  @attr user;
  @attr minutes;
  @attr ticket;
  @attr code;
  @attr billable;
}